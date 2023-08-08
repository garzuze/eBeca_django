from django.conf import settings

from product.models import Product

# Classe que será usada como carrinho de compras

class Cart(object):
    def __init__(self, request):
        """Inicia o carrinho na sesssão"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        """Relaciona as pks dos produtos com os produtos em si"""
        for key in self.cart.keys():
            self.cart[str(key)]['product'] = Product.objects.get(pk=key)

        for item in self.cart.values():
            item['total_price'] = int(item['product'].price * item['quantity']) / 100

            yield item

    def __len__(self):
        """Retorna a quantidade de produtos no carrinho"""
        return sum(item['quantity'] for item in self.cart.values())
        
    def save(self):
        """Salva os produtos no carrinho"""
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, product_id, quantity=1, update_quantity=False):
        """Adiciona os produtos no carrinho"""
        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'id': product_id}

        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)

            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)

        self.save()

    def remove(self, product_id):
        """"Remove o produto do carrinho"""
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total(self):
        for key in self.cart.keys():
            self.cart[str(key)]['product'] = Product.objects.get(pk=key)

        return int(round(sum(item['product'].price * item['quantity'] for item in self.cart.values()), 2)) / 100