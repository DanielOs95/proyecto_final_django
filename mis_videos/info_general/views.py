from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .logica_principal.servicios import insertar_usuario, insertar_video, insertar_usuario_video
from .models import Usuario, Video

# Create your views here.
def pagina_principal(request):
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
        request.session['videos'] = []

        insertar_usuario(id_nomina, nombre_usuario)

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
    cantidad_videos = request.session.get('cantidad_videos')
    videos = request.session.get('videos', [])
    id_nomina = request.session.get('id_nomina')
    nombre_usuario = request.session.get('nombre_usuario')

    usuario = Usuario.objects.get(id_nomina=id_nomina) if id_nomina else None

    if request.method == 'POST':
        nombre_video = request.POST.get("nombre_video")
        extension_video = request.POST.get("extension_video")
        tamano_video = request.POST.get("tamano_video")

        if not nombre_video or not extension_video or not tamano_video.isdigit():
            return HttpResponse("Datos incorrectos, intenta nuevamente")

        if extension_video not in [".mpg", ".mov", ".mp4", ".avi"]:
            return HttpResponse("Datos incorrectos, ingresa una extension(.mpg, .mov, .mp4, .avi)")

        tamano_video_validacion = int(tamano_video)
        if tamano_video_validacion not in range(1, 4):
            return HttpResponse("Datos incorrectos, el tamano debe ser entre 1 y3")

        if usuario:
            video = insertar_video(usuario, nombre_video, extension_video, tamano_video)
            if video:
                insertar_usuario_video(usuario, video)

        videos.append({
            'nombre_video': nombre_video,
            'extension_video': extension_video,
            'tamano_video': tamano_video,
        })
        request.session['videos'] = videos

        if len(videos) >= cantidad_videos:
            return redirect('ultima_pagina')

    video_act = len(videos) +1
    return render(request, "tercera.html", {
        "video_act": video_act,
        "cantidad_videos": cantidad_videos,
    })

def ultima_pagina(request):
    lista_usuario = Usuario.objects.all().values
    lista_video = Video.objects.all().values
    template = loader.get_template("ultima_pagina.html")
    context = {
        'lista_usuarios': lista_usuario,
        'lista_videos': lista_video
    }
    return HttpResponse(template.render(context, request))






