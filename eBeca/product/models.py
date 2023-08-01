from django.db import models
from django.core.files import File

from io import BytesIO
from PIL import Image

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
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    class Meta:
        # classe para ordernar dos produtos mais recentes para os mais velhos
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
    
    def display_price(self):
        """Mostra o preço em reais do produto (não em centavos)"""
        return int(self.price) / 100
    
    # thumbnail é a imagem num formato menor, que é utilizada na hora de listar os produtos
    def get_thumbnail(self):
        """Gera a thumbnail para ser utilizada nas páginas de compra"""
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                # retorna uma imagem genérica para caso não exista imagem do produtos
                return 'https://via.placeholder.com/240x240x.jpg'
            
    def make_thumbnail(self, image, size=(300, 300)):
        """Criar thumbnail a partir da imagem fornecida"""
        img = Image.open(image).convert('RGB').thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
