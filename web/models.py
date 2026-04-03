from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# 👤 PERFIL DE USUARIO
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_perfil(sender, instance, **kwargs):
    instance.perfil.save()



# 💼 BILLETERA
class Billetera(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saldo = models.IntegerField(default=0)

    def __str__(self):
        return f"Billetera de {self.user.username}"

# 🛒 PRODUCTO
class Producto(models.Model):
    CATEGORIAS = [
        ('polera', 'Poleras'),
        ('poleron', 'Polerones'),
        ('accesorio', 'Accesorios'),
    ]

    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    stock = models.IntegerField(default=0)
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

# 🧾 COMPRA
class Compra(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

# 💸 TRANSACCIÓN
class Transaccion(models.Model):
    billetera = models.ForeignKey(Billetera, on_delete=models.CASCADE)
    monto = models.IntegerField()
    tipo = models.CharField(max_length=10)
    fecha = models.DateTimeField(auto_now_add=True)

# 🔥 SIGNAL
@receiver(post_save, sender=User)
def crear_billetera(sender, instance, created, **kwargs):
    if created:
        Billetera.objects.create(user=instance)
        Perfil.objects.create(user=instance)

# 🛒 CARRITO
class Carrito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.producto.nombre} x {self.cantidad}"

    class Meta:
        unique_together = ('user', 'producto')
