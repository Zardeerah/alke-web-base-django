from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Producto, Carrito, Perfil
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Sum


# 🟢 INICIO


def inicio(request):
    productos = Producto.objects.filter(destacado=True)

    if request.user.is_authenticated:
        cantidad = Carrito.objects.filter(user=request.user).aggregate(
            total=Sum('cantidad')
        )['total'] or 0
    else:
        cantidad = 0

    return render(request, "web/inicio.html", {
        "productos": productos,
        "cantidad_carrito": cantidad
    })

# 🟢 LOGIN + REGISTRO (MISMO TEMPLATE)
def login_usuario(request):
    error = None

    if request.method == "POST":
        tipo = request.POST.get("tipo")

        # 🟢 LOGIN
        if tipo == "login":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                error = "Usuario o contraseña incorrectos"

        # 🟢 REGISTRO
        elif tipo == "registro":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            password2 = request.POST.get("password2")

            # 🔴 VALIDACIONES
            if password != password2:
                error = "Las contraseñas no coinciden"
            elif User.objects.filter(username=username).exists():
                error = "El usuario ya existe"
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                login(request, user)
                return redirect("inicio")

    return render(request, "web/login.html", {"error": error})


# 🛒 AGREGAR AL CARRITO
@login_required
def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    # 🚨 validar stock
    if producto.stock <= 0:
        return redirect("inicio")

    item, created = Carrito.objects.get_or_create(
        user=request.user,
        producto=producto
    )

    if not created:
        item.cantidad += 1
    else:
        item.cantidad = 1

    item.save()

    # 🔥 descontar stock
    producto.stock -= 1
    producto.save()

    return redirect("ver_carrito")


@login_required
def ver_carrito(request):
    carrito = Carrito.objects.filter(user=request.user)

    total = sum(item.producto.precio * item.cantidad for item in carrito)

    return render(request, "web/carrito.html", {
        "carrito": carrito,
        "total": total
    })


@login_required
def sumar_carrito(request, id):
    item = get_object_or_404(Carrito, id=id, user=request.user)
    producto = item.producto

    if producto.stock > 0:
        item.cantidad += 1
        item.save()

        # 🔥 descontar stock
        producto.stock -= 1
        producto.save()

    return redirect("ver_carrito")


@login_required
def restar_carrito(request, id):
    item = get_object_or_404(Carrito, id=id, user=request.user)
    producto = item.producto

    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
    else:
        item.delete()

    # 🔥 devolver stock
    producto.stock += 1
    producto.save()

    return redirect("ver_carrito")


# 🗑️ ELIMINAR PRODUCTO
@login_required
def eliminar_carrito(request, id):
    item = get_object_or_404(Carrito, id=id, user=request.user)
    producto = item.producto

    # 🔥 devolver TODO lo que tenía
    producto.stock += item.cantidad
    producto.save()

    item.delete()

    return redirect("ver_carrito")


# 🟢 CATEGORÍAS
def poleras(request):
    productos = Producto.objects.filter(categoria="polera")
    return render(request, "web/poleras.html", {"productos": productos})


def polerones(request):
    productos = Producto.objects.filter(categoria="poleron")
    return render(request, "web/polerones.html", {"productos": productos})


def accesorios(request):
    productos = Producto.objects.filter(categoria="accesorio")
    return render(request, "web/accesorios.html", {"productos": productos})


def contacto(request):
    return render(request, "web/contacto.html")


# 🟢 LOGOUT
def logout_usuario(request):
    logout(request)
    return redirect("inicio")

@login_required
def editar_perfil(request):
    perfil = request.user.perfil

    if request.method == "POST":
        # 🔹 actualizar datos del usuario (tabla User)
        request.user.email = request.POST.get("email")
        request.user.save()

        # 🔹 actualizar datos del perfil
        perfil.direccion = request.POST.get("direccion")
        perfil.telefono = request.POST.get("telefono")
        perfil.save()

        return redirect("inicio")

    return render(request, "web/editar_perfil.html", {
        "user": request.user,
        "perfil": perfil
    })

productos = Producto.objects.filter(destacado=True)

@login_required
def editar_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == "POST":
        # 🔹 actualizar email (User)
        request.user.email = request.POST.get("email")
        request.user.save()

        # 🔹 actualizar perfil
        perfil.direccion = request.POST.get("direccion")
        perfil.telefono = request.POST.get("telefono")
        perfil.save()

        return redirect("inicio")

    return render(request, "web/editar_perfil.html", {
        "user": request.user,
        "perfil": perfil
    })


@login_required
def cambiar_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('inicio')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'web/cambiar_password.html', {'form': form})
@login_required
def ver_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    return render(request, "web/perfil.html", {
        "perfil": perfil
    })
