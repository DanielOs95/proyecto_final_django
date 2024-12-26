from . import views
from django.urls import path

urlpatterns = [
    path("", views.pagina_principal, name="principal"),
    path("bienvenida", views.bienvenida, name="bienvenida")
]