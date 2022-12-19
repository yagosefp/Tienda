import json

import stripe
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from carrito.carrito import Carrito
from orders.views import pago_confirmation


def order_placed(request):
    carrito = Carrito(request)
    carrito.clear()
    return render(request, 'pago/orderplaced.html')


class Error(TemplateView):
    template_name = 'pago/error.html'


@login_required
def CarritoView(request):

    carrito = Carrito(request)
    total = str(carrito.get_total_precio())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'sk_test_51MC0gKBbI7O9XQcTqRMvT3tLAYCRM4N3cLdApW6Jgq7A8JnaEbxUNrLFneKboUKQU3WOmtzDGLWVVTwp8yzfrDJG00GYchcaBb'
    intent = stripe.PaymentIntent.create(
        amount=total*100,
        currency='eur',
        metadata={'userid': request.user.id}
    )

    return render(request, 'pago/home.html', {'client_secret': intent.client_secret})


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'pago_intent.succeeded':
        pago_confirmation(event.data.object.client_secret)

    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)