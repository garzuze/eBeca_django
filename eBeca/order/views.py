from django.shortcuts import redirect, render


# Create your views here.

from .models import Order, OrderItem
from cart.cart import Cart

def start_order(request):
    cart = Cart(request)
    total_price = 0
    
    if cart:
        for item in cart:
            product = item['product']
            total_price += product.price * int(item['quantity'])

        if request.method == 'POST':
            profile = request.user.userprofile
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            address = request.POST.get('address')
            cep = request.POST.get('cep')
            phone = request.POST.get('phone')

            # atualizando profile do usuário com informações adicionais
            profile.cep = cep
            profile.phone = phone
            profile.address = address
            profile.save()

            order = Order.objects.create(user=request.user, first_name=first_name,
                                        last_name=last_name, email=email,
                                        address=address, cep=cep, phone=phone, 
                                        paid=True, paid_amount=total_price)
            
            for item in cart:
                product = item['product']
                quantity = int(item['quantity'])
                price = product.price * quantity

                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

            cart.clear()

            return redirect('success')
    else:
        return redirect('error')
    
    return redirect('cart')

def error(request):
    return render(request, 'core/error.html')