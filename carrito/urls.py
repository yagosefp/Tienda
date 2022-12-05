from django.urls import path

from . import views

app_name='carrito'

urlpatterns = [
    path('', views.carrito_m, name='carrito_m'),
    path('add/', views.carrito_add, name='carrito_add'),
   
]