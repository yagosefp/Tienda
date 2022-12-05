from django.urls import path

from . import views

app_name ='tienda'

urlpatterns = [
    path('', views.tproductos, name='tproductos'),
    path('item/<slug:slug>/', views.detalleproducto, name='detalleproducto'),
    path('tienda/<slug:tipo_slug>/', views.listatipos, name='listatipos'),
]