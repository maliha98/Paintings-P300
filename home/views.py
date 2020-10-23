from django.shortcuts import render, redirect, reverse, get_object_or_404
from product.models import Product
from .models import Cart, Order_Product
# Create your views here.


def homeView(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'product': product})


def cartView(request):
    user = request.user
    cart_item = Cart.objects.filter(user=user, purchased=False)
    order_item = Order_Product.objects.filter(user=user, ordered=False)
    if cart_item.exists():
        order = order_item[0]
        return render(request, 'cart.html', {'cart': cart_item, 'order': order})
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
