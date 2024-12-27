from info_general.models import Usuario, Video, UsuarioVideo


def insertar_usuario(id_nomina, nombre_usuario):
    try:
        usuario = Usuario.objects.create(id_nomina=id_nomina, nombre_usuario=nombre_usuario)
        return usuario
    except Exception as e:
        print(f"Error al insertar los datos: {e}")


def insertar_video(usuario, nombre_video, extension_video, tamano_videos):
    try:
        video = Video.objects.create(
            #  usuario=usuario,
            nombre_video=nombre_video,
            extension_video=extension_video,
            tamano_videos=tamano_videos
        )
        return video
    except Exception as e:
        print(f"Error al insertar videos: {e}")



def insertar_usuario_video(usuario, video):
    try:
        usuario_video = UsuarioVideo.objects.create(
            id_nomina=usuario,
            id_video=video
        )
        return usuario_video

    except Exception as e:
        print(f"Error al relacionar videos, usuario: {e}")






