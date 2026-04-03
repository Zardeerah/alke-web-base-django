from django.contrib import admin
from .models import Producto, Carrito, Perfil, Billetera, Compra, Transaccion

admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Perfil)
admin.site.register(Billetera)
admin.site.register(Compra)
admin.site.register(Transaccion)