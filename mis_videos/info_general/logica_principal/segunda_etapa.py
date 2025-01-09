#from .servicios import insertar_usuario, insertar_video

class Persona:

    def __init__(self, id_nomina, nombre_usuario, cantidad_videos, respuesta):
        self.id_nomina = id_nomina
        self.nombre_usuario = nombre_usuario
        self.cantidad_videos = cantidad_videos
        self.respuesta = respuesta

    # esta funcion contiene el input de entrada para el numero de nomina para el empleado
    # y tambien ya contiene la validacion para evitar que se ingrese campo vacio, solo valores alfanumericos
    def num_nomina(self):
        while True:
            id_nomina = input("Ingresa tu numero de nomina: ")
            self.id_nomina = id_nomina
            if self.id_nomina.isalnum():
                return self.id_nomina
            else:
                print("Formato incorrecto, ingrese solo numeros y letras")

    # esta funcion recibe el nombre del usuario ya con validacion, solo acepta letras
    def nombre_empleado(self):
        while True:
            nombre_usuario = input("Ingresa tu nombre completo: ")
            self.nombre_usuario = nombre_usuario
            if self.nombre_usuario.replace(" ", "").isalpha():
                return self.nombre_usuario
            else:
                print("Formato incorrecto, ingrese solo letras")

    # esta funcion maneja la cantidad de videos, que se desea cargar ya con su validacion, solo cepta numeros
    def cantidad_videos_ingresados(self):
        while True:
            try:
                cantidad_videos = int(input("Ingresa la cantidad de video a subir: "))
                self.cantidad_videos = cantidad_videos
                break
            except ValueError:
                print("Formato incorrecto, ingrese solo numeros")

    # esta funcion se encarga de mostrar la informacion recopilada en los inputs
    def respuesta_valida(self):
        print(f"Bienvenido {self.nombre_usuario}, tu numero de nomina es {self.id_nomina} y estas intentando subir {self.cantidad_videos} videos, la informacion es correcta?")

    # esta funcion se encarga de manejar solo dos respuestas: si y no, y tambien contiene validacion
    # en caso que se ingrese otra respuestas y asi evitar errores en el sistema
    def respuesta_opcional(self):
        while True:
            respuesta = input("Si/No: ").lower()
            opcion = ["si", "no"]
            self.respuesta = respuesta
            if self.respuesta not in opcion:
                print("Formato incorrecto, ingrese solo (si, no)")
            else:
                return self.respuesta



persona = Persona("", "", "", "")

persona.num_nomina()
persona.nombre_empleado()
persona.cantidad_videos_ingresados()
persona.respuesta_valida()
persona.respuesta_opcional()




class Video(Persona):


    def __init__(self, id_nomina, nombre_usuario, cantidad_videos, respuesta, nombre_video, extension_video, tamano_video, lista_videos):
        super().__init__(id_nomina, nombre_usuario, cantidad_videos, respuesta)
        self.nombre_video = nombre_video
        self.extension_video = extension_video
        self.tamano_videos = tamano_video
        self.lista_videos = lista_videos

    # como su nombre lo indica esta funcion se ejecuta cuando el usuario ingresa "si" en manejar_respuesta() y luego pide los datos:
    # titulo_video, nombre, extension_video, megas_video, tambien contiene una lsta vacia "lista_videos" en la cual se insertan
    # los datos obtenidos para posteriormente retornalos y asi poder obtener dicha informacion dede otra parte donde sea requerida
    def respuesta_si(self):

        self.lista_videos = []

        if persona.respuesta == 'si':
            #usuario = insertar_usuario(persona.id_nomina, persona.nombre_usuario)
            for i in range(persona.cantidad_videos):
                print(f"Ingresa los datos del video {i + 1}")

                # aqui se realiza la validacion del nombre del video solo con valores alfanumericos
                while True:
                    nombre_video = input("Ingrese un nombre para el video: ")
                    self.nombre_video = nombre_video
                    if not self.nombre_video.replace(" ", "").isalnum():
                        print("Nombre en formato incorrecto, ingrese solo numeros y letras: ")
                    else:
                        break

                # aqui se realiza la validacion de la extension del video solo acepta los valores que se encuentran en
                # la lista extensiones (".mpg", ".mov", ".mp4", ".avi")
                while True:
                    extension_video = input("Ingresa la extension del video(.mpg, .mov, etc.): ")
                    self.extension_video = extension_video
                    extensiones = [".mpg", ".mov", ".mp4", ".avi"]
                    if self.extension_video not in extensiones:
                        print("Extension en formato incorrecto, ingrese solo extensiones(.mpg, .mov, .mp4, .avi)")
                    else:
                        break

                # aqui se realiza la validacion en megas del video solo acepta numeros y no mayor a 3
                while True:
                    tamano_video = input("Ingresa el tamano en megas del video(no mayor a 3): ")
                    self.tamano_videos = tamano_video
                    if self.tamano_videos.isdigit():
                        self.tamano_videos = int(self.tamano_videos)
                        if 0 < self.tamano_videos <= 3:
                            break
                        else:
                            print("El archivo no debe pesar mas de 3 MB")

                #insertar_video(usuario, self.nombre_video, self.extension_video, self.tamano_videos)

                # en este bloque se insertan los datos ya validados de titulo_video, nombre_video, extension_video, megas_video
                # se van a insertar a la lista vacia lista_videos
                self.lista_videos.append({
                    "nombre": nombre_video,
                    "extension_video": extension_video,
                    "tamano_videos": tamano_video
                })
                print("--Video agregado correctamente--")

            return self.lista_videos

    # como su nombre lo indica esta funcion se ejecuta cuando el usuario ingresa "no" en la funcion manejar_respuesta,
    # se le pregunta al usuario si desea salir, en caso contrario inicia un bucle  en el cual va iniciar a pedir la informacion de:
    # numero_nomina(),nombre_usuario(), cantidad_videos() hasta que el usuario ingrese que si esta bien la informacion
    def respuesta_no(self):
            while True:
                print("Desea salir del sistema?")

                while True:
                    sub_respuesta = input("Si/No: ").lower()
                    respuesta_si_no = ["si", "no"]
                    if sub_respuesta not in respuesta_si_no:
                        print("Formato incorrecto, ingrese solo (si, no)")
                    else:
                        break


                if sub_respuesta == 'si':
                    print("Gracias por usar nuestro sistema, hasta luego...")
                    break
                elif sub_respuesta == 'no':
                    persona.num_nomina()
                    persona.nombre_empleado()
                    persona.cantidad_videos_ingresados()
                    persona.respuesta_valida()
                    persona.respuesta_opcional()
                    if persona.respuesta == 'si':
                        self.respuesta_si()

    # esta funcion se encarga de crear un archivo y luego insertar los datos ya validados en id_empleado, nombre, videos, lista_videos
    # y en lista_videos

    def creacion_archivo(self):
        contenido_archivo = (
            "***********IMPRESION DE DATOS**********\n\n"
            "\nInformacion del empleado:\n"
            f"Numero de empleado: {persona.id_nomina} | "
            f"Nombre: {persona.nombre_usuario} | "
            f"Cantidad de videos: {persona.cantidad_videos} | "
        )

        contenido_archivo += "\n\nInformacion de videos:\n"
        for i, video in enumerate(self.lista_videos, start=1):
            contenido_archivo += (
                f"\nVideo {i}: \n"
                f"Nombre: {video['nombre']} | "
                f"Extension: {video['extension_video']} | "
                f"Tamano: {video['tamano_videos']} MB | "
                "\n------------------------------------------------------------------------\n"
            )
        # aqui se realiza una exception en caso de que falle al crear el archivo
        try:
            with open('../../../salida.txt', 'w') as file:
                file.write(contenido_archivo)
                print("Tiquet guardado correctamente")
        except Exception as e:
            print(f"Error  al guardar el archivo: {e}")


videos = Video("","", "", "", "", "", "", "")
videos.respuesta_si()
videos.respuesta_no()
videos.creacion_archivo()







