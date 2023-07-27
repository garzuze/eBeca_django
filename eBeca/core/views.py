from django.shortcuts import render

from product.models import Product

# Create your views here.

def frontpage(request):
    products = Product.objects.all()

    return render(request, 'core/frontpage.html', {'products': products})

def shop(request):
    products = Product.objects.all()

    return render(request, 'core/shop.html', {'products': products})