from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class Usuario(AbstractUser):
    nome = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    is_totem = models.BooleanField(default=False)

class Estoque(models.Model):
    coca = models.IntegerField()
    cerveja = models.IntegerField()
    hamburguer = models.IntegerField()

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    coca = models.IntegerField()
    cerveja = models.IntegerField()
    hamburguer = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=Pedido)
def atualizar_estoque(sender, instance, created, **kwargs):
    if created:
        estoque = Estoque.objects.first()
        estoque.coca -= instance.coca
        estoque.cerveja -= instance.cerveja
        estoque.hamburguer -= instance.hamburguer
        estoque.save()

