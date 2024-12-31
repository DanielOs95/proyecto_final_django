from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.template import loader

#from mis_videos.info_general.logica_principal.app import cantidad_videos


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
        request.session['videos'] = []

        return redirect('bienvenida')

    return redirect('pagina_principal')



'''def manejo_videos(request):
    video_i = request.session.get('video_i', 0)
    cantidad_videos = request.session.get('cantidad_videos', 0)


    if request.method == 'POST':
        nombre_video = request.POST.get("nombre_video")
        extension_video = request.POST.get("extension_video")
        tamano_video = request.POST.get("tamano_video")

        if not nombre_video or not extension_video or not tamano_video.isdigit():
            return HttpResponse("Datos incorrectos, ingrese los datos nuevamente")


        videos = request.session.get('videos', [])
        videos.append({
            'nombre_video': nombre_video,
            'extension_video': extension_video,
            'tamano_video': int(tamano_video),
        })
        request.session['videos'] = videos

        request.session['video_i'] += 1
        video_i += 1

        if video_i >= cantidad_videos:
            return redirect('ultima_pagina')


        #request.session['nombre_video'] = nombre_video
        #request.session['extension_video'] = extension_video
        #request.session['tamano_video'] = int(tamano_video)

        #return redirect('ultima_pagina')

    return render(request, "manejo_")
'''



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

    if request.method == 'POST':
        nombre_video = request.POST.get("nombre_video")
        extension_video = request.POST.get("extension_video")
        tamano_video = request.POST.get("tamano_video")

        if not nombre_video or not extension_video or not tamano_video.isdigit():
            return HttpResponse("Datos incorrectos, ingrese los datos nuevamente")


        videos.append({
            'nombre_video': nombre_video,
            'extension_video': extension_video,
            'tamano_video': int(tamano_video),
        })
        request.session['videos'] = videos

        if len(videos) == cantidad_videos:
            return redirect('ultima_pagina')

    video_act = len(videos) +1
    return render(request, "tercera.html", {
        "video_act": video_act,
        "cantidad_videos": cantidad_videos,
    })



def ultima_pagina(request):
    return render(request, "ultima_pagina.html")






