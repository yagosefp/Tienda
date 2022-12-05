from tienda.models import Producto

class Carrito():
   

    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get('token')
        if 'token' not in request.session:
            carrito = self.session['token'] = {}
        self.carrito = carrito

    def add(self, producto, cant):
        
        producto_id = str(producto.id)

        if producto_id not in self.carrito:
    
            self.carrito[producto_id] = {'precio': str(producto.precio), 'cant': int(cant)}

        self.session.modified=True

    def __len__(self):
      
     return sum(item['cant'] for item in self.carrito.values())