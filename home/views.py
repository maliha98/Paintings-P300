from django.shortcuts import render, redirect, reverse, get_object_or_404
from product.models import Product, Category
from .models import Cart, Order_Product, address
from .form import AddressForm
# Create your views here.


def homeView(request):
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'index.html', {'product': product, 'category': category})


def categoryView(request, id):

    product = Product.objects.all().filter(category_id=id)
    category = Category.objects.all()

    return render(request, 'category.html', {'product': product, 'category': category})


def cartView(request):
    user = request.user
    cart_item = Cart.objects.filter(user=user, purchased=False)
    category = Category.objects.all()
    order_item = Order_Product.objects.filter(user=user, ordered=False)
    if cart_item.exists():
        order = order_item[0]
        return render(request, 'cart.html', {'cart': cart_item, 'order': order, 'category': category})
    else:
        return render(request, 'cart.html')


def addToCart(request, id):
    product_item = get_object_or_404(Product, id=id)
    order_item, created = Cart.objects.get_or_create(
        product=product_item,
        user=request.user,
        purchased=False
    )
    o_item = Order_Product.objects.filter(user=request.user, ordered=False)
    if o_item.exists():
        order = o_item[0]

        if order.cartitem.filter(product__id=product_item.id).exists():
            order_item.quantity += 1
            order_item.save()
            return redirect("home")
        else:
            order.cartitem.add(order_item)
            return redirect("home")
    else:
        order = Order_Product.objects.create(
            user=request.user)
        order.cartitem.add(order_item)
        return redirect("home")


def plusCart(request, id):
    product_item = get_object_or_404(Product, id=id)
    order_item, created = Cart.objects.get_or_create(
        product=product_item,
        user=request.user,
        purchased=False
    )
    o_item = Order_Product.objects.filter(user=request.user, ordered=False)
    if o_item.exists():
        order = o_item[0]

        if order.cartitem.filter(product__id=product_item.id).exists():
            order_item.quantity += 1
            order_item.save()
            return redirect("cart")
        else:
            order.cartitem.add(order_item)
            return redirect("cart")
    else:
        order = Order_Product.objects.create(
            user=request.user)
        order.cartitem.add(order_item)
        return redirect("cart")


def minusCart(request, id):
    product_item = get_object_or_404(Product, id=id)
    order_item, created = Cart.objects.get_or_create(
        product=product_item,
        user=request.user,
        purchased=False
    )
    o_item = Order_Product.objects.filter(user=request.user, ordered=False)
    if o_item.exists():
        order = o_item[0]

        if order.cartitem.filter(product__id=product_item.id).exists():
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                return redirect("cart")
            else:
                order.cartitem.remove(order_item)
                order_item.delete()
                return redirect("cart")

        else:
            order.cartitem.add(order_item)
            return redirect("cart")
    else:
        order = Order_Product.objects.create(
            user=request.user)
        order.cartitem.add(order_item)
        return redirect("cart")


def removeCart(request, id):
    product_item = get_object_or_404(Product, id=id)
    order_item, created = Cart.objects.get_or_create(
        product=product_item,
        user=request.user,
        purchased=False
    )
    o_item = Order_Product.objects.filter(user=request.user, ordered=False)
    if o_item.exists():
        order = o_item[0]
        if order.cartitem.filter(product__id=product_item.id).exists():
            order.cartitem.remove(order_item)
            order_item.delete()
            return redirect("cart")
    else:
        return redirect("cart")


def address_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AddressForm()
        else:
            addr = address.objects.get(id=id)
            form = AddressForm(instance=addr)
        return render(request, "address_form.html", {'form': form})
    else:
        if id == 0:
            form = AddressForm(request.POST)
        else:
            addr = address.objects.get(id=id)
            form = AddressForm(request.POST, instance=addr)
        if form.is_valid():
            form.save()
        return redirect('checkout')


def checkout(request):

    form = AddressForm

    cart = Cart.objects.filter(user=request.user, purchased=False)

    order_qs = Order_Product.objects.filter(
        user=request.user, ordered=False)

    order_items = order_qs[0].cartitem.all()

    order_total = order_qs[0].orderTotal()

    context = {"form": form, "order_items": order_items,
               "order_total": order_total, 'cart': cart}

    saved_address = address.objects.filter(
        user=request.user)
    if saved_address.exists():
        savedAddress = saved_address.first()
        context = {"form": form, "order_items": order_items,
                   "order_total": order_total, "savedAddress": savedAddress, 'cart': cart}
    if request.method == "POST":
        saved_address = address.objects.filter(
            user=request.user)
        if saved_address.exists():

            savedAddress = saved_address.first()
            form = AddressForm(request.POST, instance=savedAddress)
            if form.is_valid():
                billingaddress = form.save(commit=False)
                billingaddress.user = request.user
                billingaddress.save()
        else:
            form = AddressForm(request.POST)
            if form.is_valid():
                billingaddress = form.save(commit=False)
                billingaddress.user = request.user
                billingaddress.save()
                return redirect('checkout')

    return render(request, 'checkout.html', context)


def payment(request):
    return render(request, 'payment.html')


def aboutPage(request):
    return render(request, 'about.html')
