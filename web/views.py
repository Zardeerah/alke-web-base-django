import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from pathlib import Path


def inicio(request):

    ruta = Path(__file__).resolve().parent / "data" / "productos.json"

    with open(ruta, encoding="utf-8") as archivo:
        datos = json.load(archivo)

    return render(request, "web/inicio.html", {
        "productos": datos["productos"]
    })


def contacto(request):
    return render(request, "web/contacto.html")


def login_usuario(request):

    if request.method == "POST":

        usuario = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=usuario, password=password)

        if user is not None:
            login(request, user)
            return redirect("inicio")

    return render(request, "web/login.html")