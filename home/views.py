from django.shortcuts import render
from product.models import Product

# Create your views here.


def homeView(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'product': product})


def aboutView(request):
    return render(request, 'about.html')
