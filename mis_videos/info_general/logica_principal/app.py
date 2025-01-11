#esta funcion contiene el input de entrada para el numero de nomina para el empleado
#y tambien ya contiene la validacion para evitar que se ingrese campo vacio, solo valores alfanumericos
def numero_nomina():
    while True:
        id_empleado = input("Ingresa tu numero de nomina: ")
        if not id_empleado.isalnum():
            print("Formato incorrecto, ingrese solo numeros y letras")
        else:
            return id_empleado

#esta funcion recibe el nombre del usuario ya con validacion, solo acepta letras
def nombre_usuario():
    while True:
        nombre = input("Ingresa tu nombre completo: ")
        if nombre.replace(" ", "").isalpha():
            return nombre
        else:
            print("Formato incorrecto, ingrese solo letras")

#esta funcion maneja la cantidad de videos, que se desea cargar ya con su validacion, solo cepta numeros
def cantidad_videos():
    videos = input("Ingresa la cantidad de videos a subir: ")
    while not(videos.isdigit()):
        print("Formato incorrecto, ingrese solo numeros")
        videos = input("Ingresa la cantidad de videos a subir: ")

    return int(videos)

#esta funcion se encarga de recopilar la informacion ingresada en:
# numero_nomina(), nombre_usuario(), cantidad_videos() y solo devuelve los valores de las funciones
def validar_informacion():
    id_empleado = numero_nomina()
    nombre = nombre_usuario()
    videos = cantidad_videos()
    print(f"Bienvenido {nombre}, tu numero de nomina es {id_empleado} y estas intentando subir {videos} videos, la informacion es correcta?")
    return id_empleado, nombre, videos

#esta funcion se encarga de manejar solo dos respuestas: si y no, y tambien contiene validacion
#en caso que se ingrese otra respuestas y asi evitar errores en el sistema
def manejar_respuesta():
    while True:
        respuesta = input("Si/No: ").lower()
        solo_si_no = ["si", "no"]
        if respuesta not in solo_si_no:
            print("Formato incorrecto, ingrese solo (si, no)")
        else:
            return respuesta

#como su nombre lo indica esta funcion se ejecuta cuando el usuario ingresa "si" en manejar_respuesta() y luego pide los datos:
#titulo_video, nombre, extension_video, megas_video, tambien contiene una lsta vacia "lista_videos" en la cual se insertan
#los datos obtenidos para posteriormente retornalos y asi poder obtener dicha informacion dede otra parte donde sea requerida
def respuesta_si(videos):
        lista_videos = []
        for i in range(videos): # aqui se realiza una iteracion despues que se valido cantidad_video() en validar_informacion()
                                # y dependiendo de cuantos videos desea subir el cliente es la cantidad de veces que se pedira:
                                #titulo_video, nombre_video y extension_video


            #aqui se realiza la validacion del titulo del video solo con valores alfanumericos
            while True:
                titulo_video = input("Ingresa un titulo para el video: ")
                if not titulo_video.replace(" ", "").isalnum():
                    print("Titulo en formato incorrecto, ingrese solo numeros y letras")
                else:
                    break

            # aqui se realiza la validacion del nombre del video solo con valores alfanumericos
            while True:
                nombre_video = input("Ingresa un nombre para el video: ")
                if not nombre_video.replace(" ", "").isalnum():
                    print("Nombre en formato incorrecto, ingrese solo numeros y letras: ")
                else:
                    break

            # aqui se realiza la validacion de la extension del video solo acepta los valores que se encuentran en
            # la lista extensiones (".mpg", ".mov", ".mp4", ".avi")
            while True:
                extension_video = input("Ingresa la extension del video(.mpg, .mov, etc.): ")
                extensiones = [".mp4", ".avi", ".mov", ".wmv", ".mkv", ".webm", ".flv", ".mov"]
                if extension_video not in extensiones:
                    print("Extension en formato incorrecto, ingrese solo extensiones(.mpg, .mov, .mp4, .avi)")
                else:
                    break

            # aqui se realiza la validacion en megas del video solo acepta numeros y no mayor a 3
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

            #en este bloque se insertan los datos ya validados de titulo_video, nombre_video, extension_video, megas_video
            #se van a insertar a la lista vacia lista_videos
            lista_videos.append({
                "titulo": titulo_video,
                "nombre": nombre_video,
                "extension": extension_video,
                "tamano": megas_video
            })

        return lista_videos


#como su nombre lo indica esta funcion se ejecuta cuando el usuario ingresa "no" en la funcion manejar_respuesta,
#se le pregunta al usuario si desea salir, en caso contrario inicia un bucle  en el cual va iniciar a pedir la informacion de:
#numero_nomina(),nombre_usuario(), cantidad_videos() hasta que el usuario ingrese que si esta bien la informacion
def respuesta_no(respuesta,):
    #respuesta = manejar_respuesta()
    if respuesta == 'no':
        while True: #aqui inicia el bucle
            print("Desea salir del sistema?")

            while True:
                sub_response = input("Si/No: ") #aqui se crea una variable con un input dentro del bucle la cual esta validada para
                solo_si_no = ["si", "no"]       #solo aceptar (si, no)
                if sub_response not in solo_si_no:
                    print("Formato incorrecto, ingrese solo (si, no)")
                else:
                    break

            # si la respuesta ingresada en sub_response es si, se rompe el ciclo y se sale del bucle
            if sub_response == 'si':
                print("Gracias por usar nuestro sistema, hasta luego...")
                break
            elif sub_response == 'no':   # si la respuesta ingresada en sub_response es no, se usa la tecnica de desempaquetado para obtener
                id_empleado, nombre, videos = validar_informacion()  # los valores de la funcion validar_informacion() y manejar_respuesta()
                respuesta  = manejar_respuesta()
                #si la respuesta ingresada en respuesta de la funcion manejar_respuesta() es si, se valida y se obtine los valores de la lista lista_videos
                #para poder crear el archivo txt
                if respuesta == "si":
                    lista_videos = respuesta_si(videos)
                    crear_archivo(id_empleado, nombre, videos, lista_videos)


#esta funcion se encarga de crear un archivo y luego insertar los datos ya validados en id_empleado, nombre, videos, lista_videos
#y en lista_videos
def crear_archivo(id_empleado, nombre, videos, lista_videos):
    contenido_archivo = (
        "***********IMPRESION DE DATOS**********\n\n"
        "Informacion del empleado:\n"
        f"Numero de empleado: {id_empleado} | " 
        f"Nombre: {nombre} | "
        f"Cantidad de videos: {videos} | "
    )

    contenido_archivo += "\n\nInformacion de videos:\n"
    for i, video in enumerate(lista_videos, start=1):
        contenido_archivo += (
            f"Video {i}:\n"
            f"Titulo: {video['titulo']} | "
            f"Nombre: {video['nombre']} | "
            f"Extension: {video['extension']} | "
            f"Tamano: {video['tamano']} MB | "
            "\n___________________________________________________________________________\n"
        )

#aqui se realiza ua exception en caso de que falle al crear el archivo
    try:
        with open('../../../salida.txt', 'w') as file:
            file.write(contenido_archivo)
            print("Tiquet guardado correctamente")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")


#esta funcion se encarga de inciar todas las funciones de la app
def iniciar_app():
    id_empleado, nombre, videos = validar_informacion()
    respuesta = manejar_respuesta()


    if respuesta == 'si':
        lista_videos = respuesta_si(videos)
        crear_archivo(id_empleado, nombre, videos, lista_videos)
    else:
        respuesta_no(respuesta,)


iniciar_app()








