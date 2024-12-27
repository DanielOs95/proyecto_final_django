from . import views
from django.urls import path

from .views import manejo_datos

urlpatterns = [
    path("", views.pagina_principal, name="principal"),
    path('manejo_datos/', manejo_datos, name='manejo_datos'),
    path("bienvenida", views.bienvenida, name="bienvenida"),
    path("tercera", views.tercera_pagina, name="tercera"),
]