class Persona:

    def __init__(self, id_nomina, nombre, cantidad_videos):
        self.__id_nomina = id_nomina
        self.__nombre = nombre
        self.__cantidad_videos = cantidad_videos

    @property
    def id_nomina(self):
        return self.__id_nomina

    @property
    def nombre(self):
        return self.__nombre

    @property
    def cantidad_videos(self):
        return self.__cantidad_videos

    @id_nomina.setter
    def id_nomina(self, value):
        self.__id_nomina = value

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @cantidad_videos.setter
    def cantidad_videos(self, value):
        self.__cantidad_videos = value


    def num_nomina(self):
        id_nomina = input("Ingresa tu numero de nomina: ")
        return id_nomina


    def nombre_empleado(self):
        nombre = input("Ingresa tu nombre completo: ")
        return nombre


    def num_videos(self):
        cantidad_videos = input("Ingresa la cantidad de videos a subir: ")
        while not cantidad_videos.isdigit():
            print("Formato incorrecto, ingrese solo numeros")
            cantidad_videos = input("Ingresa la cantidad de videos a subir: ")
        return int(cantidad_videos)


    def opcion_respuesta(self):
        print(f"Bienvenido {self.__nombre}, tu numero de nomina es {self.__id_nomina} y estas intentando subir {self.__cantidad_videos} videos, la informacion es correcta?")
        respuesta = input("Si/No: ")
        return respuesta

    def crear_archivo(self):
        print("\n**********DETALLES**********")
        print(f"ID de empleado: {self.__id_nomina}")
        print(f"Nombre: {self.__nombre}")
        print(f"Cantidad de videos: {self.__cantidad_videos}")




class Videos(Persona):

    def __init__(self, id_nomina, nombre, cantidad_videos, nom_video, ext_video, tam_video):
        super().__init__(id_nomina, nombre, cantidad_videos)
        self.__nom_videos = nom_video
        self.__ext_video = ext_video
        self.__tam_video = tam_video


    @property
    def nom_video(self):
        return self.__nom_videos
    @property
    def ext_video(self):
        return self.__ext_video
    @property
    def tam_video(self):
        return self.__tam_video

    @nom_video.setter
    def nom_video(self, value):
        self.__nom_videos = value
    @ext_video.setter
    def ext_video(self, value):
        self.__ext_video = value
    @tam_video.setter
    def tam_video(self, value):
        self.__tam_video = value


    def respuesta_si(self):
        lista_videos = []

        for i in range(self.cantidad_videos):
            nom_video = input("Ingresa un nombre para el video: ")
            ext_video = input("Ingresa la extension del video(.mpg, .mov, etc.): ")
            tam_video = input("Ingresa el tamano en megas del video(no mayor a 3): ")

            lista_videos.append({
                "nombre": nom_video,
                "extension": ext_video,
                "tamano": tam_video

            })

        return lista_videos

            #videos = Videos(self.id_nomina, self.nombre, self.cantidad_videos, nom_video, ext_video, tam_video)






persona = Persona("", "", "")
persona.id_nomina = persona.num_nomina()
persona.nombre = persona.nombre_empleado()
persona.cantidad_videos = persona.num_videos()
persona.opcion_respuesta()


videos = Videos(persona.id_nomina, persona.nombre, persona.cantidad_videos,"", "", "")
videos.cantidad_videos = persona.cantidad_videos
videos.respuesta_si()





