
from decimal import Decimal

from django.conf import settings

from tienda.models import Producto

class Carrito():
   

    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get(settings.CARRITO_SESSION_ID)
        if settings.CARRITO_SESSION_ID not in request.session:
            carrito = self.session[settings.CARRITO_SESSION_ID] = {}
        self.carrito = carrito

    def add(self, producto, cant):
        
        producto_id = (producto.id)

        if producto_id  in self.carrito:
            self.carrito[producto_id]['cant'] = cant
        else:
            self.carrito[producto_id] = {'precio': int(producto.precio), 'cant': int(cant)}

        self.save()

    def __len__(self):
      
        return sum(item['cant'] for item in self.carrito.values())

    def __iter__(self):

        #Recoge los ids de los productos de una sesion y devuelve  los productos

        producto_ids = self.carrito.keys()
        productos = Producto.productos.filter(id__in=producto_ids)
        carrito = self.carrito.copy()

        for producto in productos:
            carrito[str(producto.id)]['producto'] = producto

        for item in carrito.values():
            item['precio'] = Decimal(item['precio'])
            item['total_precio'] =  item['precio'] * item['cant']
            yield item



    def actu(self, producto, cant):
        
        producto_id = str(producto)
        if producto_id in self.carrito:
            self.carrito[producto_id]['cant'] = cant
        self.save()

    def get_total_precio(self):
        total =sum(Decimal(item['precio']) * item['cant'] for item in self.carrito.values())
        return total

  

    def elim(self, producto):
      
        producto_id = str(producto)

        if producto_id in self.carrito:
            del self.carrito[producto_id]
            print(producto_id)
            self.save()

    def clear(self):
        del self.session[settings.CARRITO_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True