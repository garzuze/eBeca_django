from django.shortcuts import render

from .cart import Cart

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits

    return render(request, 'cart/menu_cart.html')

def cart(request):
    return render(request, 'cart/cart.html')