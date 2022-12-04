from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Tipo(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural ='tipos'

    def get_absolute_url(self):
        return reverse('tienda:listatipos', args=[self.slug])
    def __str__(self):
        return self.name
    
class Producto(models.Model):
    tipo = models.ForeignKey(Tipo, related_name='producto', on_delete=models.CASCADE)
    creador =models.ForeignKey(User, on_delete=models.CASCADE ,related_name='creador_producto')
    nombre = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
   
    

    class Meta:
        verbose_name_plural = 'Productos'
        ordering = ('-creado',)
    
    def get_absolute_url(self):
        return reverse('tienda:detalleproducto', args=[self.slug])

    def __str__(self):
        return self.nombre

  


# Create your models here.
