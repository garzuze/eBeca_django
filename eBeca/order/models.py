from django.db import models
from django.contrib.auth.models import User

from product.models import Product

# Create your models here.

class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')

    )

    user = models.ForeignKey(User, related_name='orders', blank=True, null=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    cep = models.IntegerField()
    address = models.CharField(max_length=255)
    phone = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_ammount = models.IntegerField(blank=True, null=True)


    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)