class Persona:

    def __init__(self, id_nomina, nombre_usuario, cantidad_videos, respuesta):
        self.id_nomina = id_nomina
        self.nombre_usuario = nombre_usuario
        self.cantidad_videos = cantidad_videos
        self.respuesta = respuesta


    def num_nomina(self):
        id_nomina = input("Ingresa tu numero de nomina: ")
        self.id_nomina = id_nomina

    def nombre_empleado(self):
        nombre_usuario = input("Ingresa tu nombre completo: ")
        self.nombre_usuario = nombre_usuario

    def cantidad_videos_ingresados(self):
        cantidad_videos = int(input("Ingresa la cantidad de video a subir: "))
        self.cantidad_videos = cantidad_videos

    def respuesta_valida(self):
        print(f"Bienvenido {self.nombre_usuario}, tu numero de nomina es {self.id_nomina} y estas intentando subir {self.cantidad_videos} videos, la informacion es correcta?")

    def respuesta_opcional(self):
        respuesta = input("Si/No: ")
        self.respuesta = respuesta


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


    def respuesta_si(self):

        self.lista_videos = []

        if persona.respuesta == 'si':
            for i in range(persona.cantidad_videos):
                nombre_video = input("Ingrese un nombre para el video: ")
                self.nombre_video = nombre_video

                extension_video = input("Ingresa la extension del video(.mpg, .mov, etc.): ")
                self.extension_video = extension_video

                tamano_video = int(input("Ingresa el tamano en megas del video(no mayor a 3): "))
                self.tamano_videos = tamano_video

                self.lista_videos.append({
                    "nombre": nombre_video,
                    "extension_video": extension_video,
                    "tamano_videos": tamano_video
                })
                print("-Video agregado correctamente-")
            return self.lista_videos


    def respuesta_no(self):

        #if persona.respuesta == 'no':
            while True:
                print("Desea salir del sistema?")
                sub_respuesta = input("Si/No: ")
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
            with open('salida.txt', 'w') as file:
                file.write(contenido_archivo)
                print("Tiquet guardado correctamente")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")


videos = Video("","", "", "", "", "", "", "")
videos.respuesta_si()
videos.respuesta_no()
videos.creacion_archivo()







