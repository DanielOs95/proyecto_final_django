from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def pagina_principal(request):
    template = loader.get_template("principal.html")
    return HttpResponse(template.render())

def bienvenida(request):
    template = loader.get_template("segunda.html")
    return HttpResponse(template.render())



