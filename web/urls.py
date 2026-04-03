from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('login/', views.login_usuario, name='login'),

    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('sumar/<int:id>/', views.sumar_carrito, name='sumar_carrito'),
    path('restar/<int:id>/', views.restar_carrito, name='restar_carrito'),
    path('eliminar/<int:id>/', views.eliminar_carrito, name='eliminar_carrito'),

    path('contacto/', views.contacto, name='contacto'),  # 🔥 ESTA FALTABA

    path('poleras/', views.poleras, name='poleras'),
    path('polerones/', views.polerones, name='polerones'),
    path('accesorios/', views.accesorios, name='accesorios'),
    path('logout/', views.logout_usuario, name='logout'),
    path('password/', views.cambiar_password, name='cambiar_password'),
    path('editar.perfil/', views.editar_perfil, name='editar_perfil'),
    path('perfil/', views.ver_perfil, name='ver_perfil'),
    path('cambiar-password/', views.cambiar_password, name='cambiar_password'),


   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)