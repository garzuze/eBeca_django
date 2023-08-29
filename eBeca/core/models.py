from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cep = models.CharField(max_length=8, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=11)  

    def __str__(self):
        return self.user.username

# Capturando um sinal
# Nós utilizamos dados do usuário recém criados para criar uma extensão do user (profile)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
