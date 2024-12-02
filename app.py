def numero_nomina():
    while True:
        id_empleado = input("Ingresa tu numero de nomina: ")
        if not id_empleado.isalnum():
            print("Formato incorrecto, ingrese solo numeros y letras")
        else:
            return id_empleado



def nombre_usuario():
    while True:
        nombre = input("Ingresa tu nombre completo: ")
        if nombre.replace(" ", "").isalpha():
            return nombre
        else:
            print("Formato incorrecto, ingrese solo letras")

def cantidad_videos():
    videos = input("Ingresa la cantidad de videos a subir: ")
    while not(videos.isdigit()):
        print("Formato incorrecto, ingrese solo numeros")
        videos = input("Ingresa la cantidad de videos a subir: ")

    return int(videos)


def validar_informacion():
    id_empleado = numero_nomina()
    nombre = nombre_usuario()
    videos = cantidad_videos()
    print(f"Bienvenido {nombre}, tu numero de nomina es {id_empleado} y estas intentando subir {videos} videos, la informacion es correcta?")
    return id_empleado, nombre, videos

#validar_informacion()
def manejar_respuesta():
    respuesta = input("Si/No: ")
    return respuesta

def respuesta_si():
        lista_videos = []
        for i in range(cantidad_videos()):

            while True:
                titulo_video = input("Ingresa un titulo para el video: ")
                if not titulo_video.isalnum():
                    print("Titulo en formato incorrecto, ingrese solo numeros y letras")
                else:
                    break

            while True:
                nombre_video = input("Ingresa un nombre para el video: ")
                if not nombre_video.isalnum():
                    print("Nombre en formato incorrecto, ingrese solo numeros y letras: ")
                else:
                    break

            while True:
                extension_video = input("Ingresa la extension del video(.mpg, .mov, etc.): ")
                extensiones = [".mpg", ".mov", ".mp4", ".avi"]
                if extension_video not in extensiones:
                    print("Extension en formato incorrecto, ingrese solo extensiones(.mpg, .mov, .mp4, .avi)")
                else:
                    break


            while True:
                megas_video = input("Ingresa el tamano en megas del video(no mayor a 3): ")
                if megas_video.isdigit():
                    megas_video = int(megas_video)
                    if 0 < megas_video <= 3:
                        break
                    else:
                        print("El archivo no debe pesar mas de 3 MB")

                else:
                    print("Tamano en formato incorrecto,  Ingrese solo numeros")


            lista_videos.append({
                "titulo": titulo_video,
                "nombre": nombre_video,
                "extension": extension_video,
                "tamano": megas_video
            })

        return lista_videos

#info_videos = respuesta_si()
#crear_archivo(id_empleado, nombre, videos, lista_videos)
#respuesta_si()

def respuesta_no(id_empleado, nombre, videos):
    #respuesta = manejar_respuesta()
    if manejar_respuesta() == 'no':
        while True:
            print("Desea salir del sistema?")
            sub_response = input("Si/No: ")

            if sub_response == 'si':
                print("Gracias por usar nuestro sistema, hasta luego...")
                break
            elif sub_response == 'no':
                id_empleado, nombre, videos = validar_informacion()
                respuesta  = manejar_respuesta()

                if respuesta == "si":
                    lista_videos = respuesta_si()
                    crear_archivo(id_empleado, nombre, videos, lista_videos)

    #respuesta_no(id_empleado, nombre, videos)

def crear_archivo(id_empleado, nombre, videos, lista_videos):
    contenido_archivo = (
        "*******IMPRESION DE DATOS******\n"
        f"Numero de empleado: {id_empleado}\n" 
        f"Nombre: {nombre}\n"
        f"Cantidad de videos: {videos}\n"
        "_____________________________________\n"
    )

    contenido_archivo += "Informacion de videos:\n"
    #enumerar_videos = 1
    for i in lista_videos:
        contenido_archivo += (
            #f"Video {i}:\n"
            f"Titulo: {i['titulo']}\n"
            f"Nombre: {i['nombre']}\n"
            f"Extension: {i['extension']}\n"
            f"Tamano: {i['tamano']}\n"
            "********************************\n"
        )
        #enumerar_videos += 1

    try:
        with open('salida.txt', 'w') as file:
            file.write(contenido_archivo)
            print("Tiquet guardado correctamente")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")



def iniciar_app():
    id_empleado, nombre, videos = validar_informacion()
    respuesta = manejar_respuesta()

    if respuesta == 'si':
        lista_videos = respuesta_si()
        crear_archivo(id_empleado, nombre, videos, lista_videos)
    else:
        #respuesta == 'no':
        respuesta_no(id_empleado, nombre, videos)


iniciar_app()








