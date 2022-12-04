
class Carrito():
   

    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get('token')
        if 'token' not in request.session:
            carrito = self.session['token'] = {}
        self.carrito = carrito