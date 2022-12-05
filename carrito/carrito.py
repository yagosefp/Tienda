
from decimal import Decimal

from tienda.models import Producto

class Carrito():
   

    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get('key')
        if 'key' not in request.session:
            carrito = self.session['key'] = {}
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
            item['total_precio'] = item['precio'] * item['cant']
            yield item



    def actu(self, producto, cant):
        
        producto_id = str(producto)
        if producto_id in self.carrito:
            self.carrito[producto_id]['cant'] = cant
        self.save()

    def get_total_precio(self):
        return sum(Decimal(item['precio']) * item['cant'] for item in self.carrito.values())

    def elim(self, producto):
      
        producto_id = str(producto)

        if producto_id in self.carrito:
            del self.carrito[producto_id]
            print(producto_id)
            self.save()

    def save(self):
        self.session.modified = True