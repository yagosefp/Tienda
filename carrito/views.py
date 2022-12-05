from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from tienda.models import Producto
from .carrito import Carrito

def carrito_m (request):
    return render(request,'tienda/carrito/muestra.html')

def carrito_add(request):
    carrito = Carrito(request)
    if request.POST.get('action') == 'post':
        producto_id = int(request.POST.get('productoid'))
        producto_cant = int(request.POST.get('productocant'))
        producto = get_object_or_404(Producto, id=producto_id)
        carrito.add(producto=producto, cant=producto_cant)

        carrito_cant = carrito.__len__()
        response = JsonResponse({'cant': carrito_cant})
        return response

