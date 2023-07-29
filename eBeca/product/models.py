from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        # classe para ordenar as categorias em ordem alfabética
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    class Meta:
        # classe para ordernar dos produtos mais recentes para os mais velhos
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
    
    def display_price(self):
        return int(self.price) / 100