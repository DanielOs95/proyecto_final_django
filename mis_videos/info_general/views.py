from django.shortcuts import render, redirect
from  django.http import HttpResponse
from  django.template import loader
from .models import Usuario, Video, UsuarioVideo
from .forms import UsuarioForm, VideoForm

#aqui se encuentra la logica que maneja la tercer pagina (se piden los datos de los usuarios, id_nomina y nombre usuario)
def principal(request):
   if request.method == "POST":
       form = UsuarioForm(request.POST)
       if form.is_valid():

           id_nomina = form.cleaned_data['id_nomina']
           nombre_usuario = form.cleaned_data['nombre_usuario']
           video = form.cleaned_data['video']

           request.session['id_nomina'] = id_nomina
           request.session['nombre_usuario'] = nombre_usuario


           form.save()
           request.session['video'] = int(video)
           return redirect('bienvenida')

   else:
       form = UsuarioForm()
   return render(request, 'principal.html', {'form': form})

#aqui se encuentra la logica que maneja la segunda pagina que da la bienvenida
def bienvenida(request):
    id_nomina = request.session['id_nomina']
    nombre_usuario = request.session['nombre_usuario']
    video = request.session['video']
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        if respuesta == 'si':
            return redirect('pagina_videos')
        else:
            return redirect('principal')

    return render(request, 'bienvenida.html', {"id_nomina": id_nomina, "nombre_usuario": nombre_usuario, "video": video})

#aqui se encuentra la logica que maneja la tercer pagina (se piden los datos de los videos, nombre_video, extension_video y tamano_video)
def pagina_videos(request):
    if request.method == "POST":
        id_nomina = request.session.get('id_nomina')
        video = request.session.get('video')
        usuario = Usuario.objects.get(id_nomina=id_nomina)
        forms = []
        for i in range(video):
            form = VideoForm(request.POST, prefix=f"video_{i}")
            if form.is_valid():
                video_insertar = form.save()
                UsuarioVideo.objects.create(usuario=usuario, video=video_insertar)
            else:
                forms.append(form)

        if all(form.is_valid() for form in forms):
            return redirect('ultima_pagina')
    else:
        video = request.session.get('video')
        forms = [VideoForm(prefix=f"video_{i}") for i in range(video)]

    return render(request, 'pagina_videos.html', {'forms': forms})

#aqui se encuentra la logica que maneja la ultima pagina se muestran toda la informacion de la base de datos, en tablas
def ultima_pagina(request):
    lista_usuario = Usuario.objects.all().values()
    lista_video = Video.objects.all().values()
    lista_usuario_video = UsuarioVideo.objects.all()
    template = loader.get_template("ultima_pagina.html")
    context = {
        'lista_usuarios': lista_usuario,
        'lista_videos': lista_video,
        'lista_usuario_videos': lista_usuario_video
    }
    return HttpResponse(template.render(context, request))











