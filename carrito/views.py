from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from tienda.models import Producto
from .carrito import Carrito

def carrito_m (request):
    carrito=Carrito(request)
    return render(request,'tienda/carrito/muestra.html',{'carrito':carrito})

def carrito_add(request):
    carrito = Carrito(request)
    if request.POST.get('action') == 'post':
        producto_id = int(request.POST.get('productoid'))
        producto_cant = int(request.POST.get('productocant'))
        producto = get_object_or_404(Producto, id=producto_id)
        carrito.add(producto=producto, cant=producto_cant)

        carritocant = carrito.__len__()
        response = JsonResponse({'cant': carritocant})
        return response

def carrito_elim(request):
    carrito = Carrito(request)
    if request.POST.get('action') == 'post':
        producto_id = int(request.POST.get('productoid'))
        carrito.elim(producto=producto_id)

        carritocant = carrito.__len__()
        carritototal = carrito.get_total_precio()
        response = JsonResponse({'cant': carritocant, 'subtotal': carritototal})
        return response


def carrito_actu(request):
    carrito = Carrito(request)
    if request.POST.get('action') == 'post':
        producto_id = int(request.POST.get('productoid'))
        producto_cant = int(request.POST.get('productocant'))
        carrito.actu(producto=producto_id, cant=producto_cant)

        carritocant = carrito.__len__()
        carritototal = carrito.get_total_precio()
        response = JsonResponse({'cant': carritocant, 'subtotal': carritototal})
        return response
