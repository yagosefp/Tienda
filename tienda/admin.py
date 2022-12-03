from django.contrib import admin

from .models import Tipo,Producto

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=['nombre','creador','slug','precio','in_stock','creado','modificado']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['precio', 'in_stock']
    prepopulated_fields = {'slug': ('nombre',)}
