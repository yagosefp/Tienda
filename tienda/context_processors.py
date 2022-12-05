from .models import Tipo


def tipos(request):
    return {
        'tipos': Tipo.objects.all()
    }