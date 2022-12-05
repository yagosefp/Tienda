from django.urls import path

from . import views

app_name='carrito'

urlpatterns = [
    path('', views.carrito_m, name='carrito_m'),
    path('add/', views.carrito_add, name='carrito_add'),
    path('elim/', views.carrito_elim, name='carrito_elim'),
    path('actu/', views.carrito_actu, name='carrito_actu'),
   
]