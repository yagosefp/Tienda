from decimal import Decimal
from django.conf import settings
from django.db import models

from tienda.models import Producto


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user')
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=250)
    ciudad = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    postal = models.CharField(max_length=20)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    order_key = models.CharField(max_length=200)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ('-creado',)
    
    def __str__(self):
        return str(self.creado)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)