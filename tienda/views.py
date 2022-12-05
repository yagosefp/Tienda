from django.shortcuts import get_object_or_404, render

from .models import Tipo,Producto

# Create your views here.

def tproductos(request):
    productos =Producto.productos.all()
    return render(request, 'tienda/home.html', {'productos': productos})

def tipos(request):
   return{
    'tipos':Tipo.objects.all()
   }
def detalleproducto(request, slug):
    producto = get_object_or_404(Producto, slug=slug, in_stock=True)
    return render(request, 'tienda/productos/detalle.html', {'producto': producto})

def listatipos(request, tipo_slug=None):
    tipo = get_object_or_404(Tipo, slug=tipo_slug)
    productos = Producto.objects.filter(tipo=tipo)
    return render(request, 'tienda/productos/tipo.html', {'tipo': tipo, 'productos': productos})