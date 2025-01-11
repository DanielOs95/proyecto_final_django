from . import views
from django.urls import path

urlpatterns = [
    path("", views.principal, name="principal"),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path("pagina_videos/", views.pagina_videos, name="pagina_videos"),
    path("ultima_pagina", views.ultima_pagina, name="ultima_pagina"),
]
