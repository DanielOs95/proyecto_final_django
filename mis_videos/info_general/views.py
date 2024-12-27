from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
#from logica_principal.servicios import insertar_usuario, insertar_video, insertar_usuario_video
#from ..info_general.logica_principal.segunda_etapa import respuesta_si
#from models import Usuario, Video, UsuarioVideo

# Create your views here.
def pagina_principal(request):
    #template = loader.get_template("principal.html")
    return render(request, "principal.html")


def manejo_datos(request):
    if request.method == "POST":
        id_nomina = request.POST.get("id_nomina")
        nombre_usuario = request.POST.get("nombre_usuario")
        cantidad_videos = request.POST.get("cantidad_videos")

        if not id_nomina or not nombre_usuario or not cantidad_videos.isdigit():
            return HttpResponse("Datos incorrectos, intenta nuevamente")

        request.session['id_nomina'] = id_nomina
        request.session['nombre_usuario'] = nombre_usuario
        request.session['cantidad_videos'] = int(cantidad_videos)

        return redirect('bienvenida')

    return redirect('pagina_principal')




def bienvenida(request):
    id_nomina = request.session.get('id_nomina')
    nombre_usuario = request.session.get('nombre_usuario')
    cantidad_videos = request.session.get('cantidad_videos')

    if request.method == 'POST':
        respuesta = request.POST.get("respuesta")
        if respuesta == "si":
            return redirect('tercera')
        else:
            return redirect("principal")

    return render(request, "segunda.html", {
        "id_nomina": id_nomina,
        "nombre_usuario": nombre_usuario,
        "cantidad_videos": cantidad_videos
    })


def tercera_pagina(request):
    return render(request, "tercera.html")



