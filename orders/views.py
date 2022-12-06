from django.http.response import JsonResponse
from django.shortcuts import render

from carrito.carrito import Carrito

from .models import Order, OrderItem


def add(request):
    carrito = Carrito(request)
    if request.POST.get('action') == 'post':

        order_key = request.POST.get('order_key')
        user_id = request.user.id
        carritototal = carrito.get_total_precio()

        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(user_id=user_id, nombre='name', direccion='dir',
                                 total=carritototal, order_key=order_key)
            order_id = order.pk

            for item in carrito:
                OrderItem.objects.create(order_id=order_id, producto=item['producto'], precio=item['precio'], cantidad=item['cant'])

        response = JsonResponse({'success': 'Return something'})
        return response


def pago_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return 