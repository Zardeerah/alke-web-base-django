# Alke Web Base - Proyecto Django

Este proyecto consiste en el desarrollo de una aplicación web utilizando el framework Django en Python. Su objetivo es implementar una solución funcional que integre base de datos, modelos, vistas y templates, aplicando el uso del ORM y operaciones CRUD.

## 🐱 Tecnologías utilizadas

- Python
- Django
- SQLite (Base de datos)
- HTML
- CSS
- Bootstrap
- Visual Studio Code

## 🐱 Funcionalidades del proyecto

- Sistema de autenticación de usuarios (registro, inicio de sesión y cierre de sesión)
- Visualización de productos por categorías
- Carrito de compras dinámico
- Cálculo automático del total de compra
- Gestión de stock de productos
- Subida y visualización de imágenes desde la base de datos
- Edición de perfil de usuario (email, dirección y teléfono)
- Cambio de contraseña
- Implementación de operaciones CRUD mediante el ORM de Django

## 🐱 Operaciones CRUD implementadas

- Crear: Registro de usuarios y agregado de productos al carrito
- Leer: Visualización de productos, carrito y perfil
- Actualizar: Edición de perfil y modificación de cantidades en el carrito
- Eliminar: Eliminación de productos del carrito

## 🐱 Estructura del proyecto

El proyecto está organizado en los siguientes componentes:

- models.py: definición de modelos y relaciones
- views.py: lógica de la aplicación
- urls.py: configuración de rutas
- templates: vistas HTML
- static: archivos CSS e imágenes
- media: almacenamiento de imágenes subidas

## 🐱 Objetivo del proyecto

Desarrollar una aplicación web funcional que permita gestionar información persistente utilizando Django y su ORM, integrando correctamente modelos, vistas y templates, y aplicando operaciones CRUD.

## 🐱 Cómo ejecutar el proyecto

1. Clonar el repositorio  
   git clone https://github.com/Zardeerah/alke-web-base-django.git

2. Ingresar al directorio del proyecto  
   cd alke-web-base-django

3. Crear entorno virtual  
   python -m venv venv

4. Activar entorno virtual (Windows)  
   venv\Scripts\activate

5. Instalar dependencias  
   pip install django

6. Aplicar migraciones  
   python manage.py makemigrations  
   python manage.py migrate

7. Ejecutar servidor  
   python manage.py runserver

8. Acceder desde el navegador  
   http://127.0.0.1:8000/

## 🐱 Autora

Paola Stuardo

Proyecto desarrollado como parte del módulo de Desarrollo Web con Django.

## 🐱 Link página en Render

https://alke-web-base-django-5.onrender.com/
