from django.urls import path

from . import views

app_name = 'pago'

urlpatterns = [
    path('', views.CarritoView, name='carrito'),
    path('orderplaced/', views.order_placed, name='order_placed'),
    path('error/', views.Error.as_view(), name='error'),
    path('webhook/', views.stripe_webhook),
]