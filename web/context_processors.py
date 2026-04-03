from .models import Carrito

def carrito_total(request):
    if request.user.is_authenticated:
        items = Carrito.objects.filter(user=request.user)
        total = sum(item.cantidad for item in items)
        return {"carrito_count": total}
    return {"carrito_count": 0}