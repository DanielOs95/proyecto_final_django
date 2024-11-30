def numero_nomina():
    id_empleado = int(input("Ingresa tu numero de nomina: "))
    return id_empleado

def nombre_usuario():
    nombre = input("Ingresa tu nombre completo: ")
    return nombre

def cantidad_videos():
    videos = int(input("Ingresa la cantidad de videos a subir: "))
    return videos


def validar_informacion():
    id_empleado = numero_nomina()
    nombre = nombre_usuario()
    videos = cantidad_videos()
    print(f"Bienvenido {nombre}, tu numero de nomina es {id_empleado} y estas intentando subir {videos} videos, la informacion es correcta?")
    return id_empleado, nombre, videos

validar_informacion()
def manejar_respuesta():
    respuesta = input("Si/No: ")
    return respuesta

def respuesta_si():
    #respuesta = manejar_respuesta()

    if manejar_respuesta() == 'si':
        for i in range(cantidad_videos()):
            titulo_video = input("Ingresa un titulo para el video: ")
            nombre_video = input("Ingresa un nombre para el video: ")
            extension_video = input("Ingresa la extension del video(.mpg, .mov, etc.): ")
            megas_video = int(input("Ingresa el tamano en megas del video(no mayor a 3): "))

#respuesta_si()

def respuesta_no():
    #respuesta = manejar_respuesta()
    if manejar_respuesta() == 'no':
        while True:
            print("Desea salir del sistema?")
            sub_response = input("Si/No: ")

            if sub_response == 'si':
                print("Gracias por usar nuestro sistema, hasta luego...")
                break
            else:
                #sub_response == 'no':
                #numero_nomina()
                #nombre_usuario()
                #cantidad_videos()
                validar_informacion()
                manejar_respuesta()
                respuesta_si()


respuesta_no()

def crear_archivo(id_empleado, nombre, videos):
    contenido_archivo = (
        "*******IMPRESION DE DATOS******\n"
        f"Numero de empleado: {id_empleado}\n" 
        f"Nombre: {nombre}\n"
        f"Cantidad de videos: {videos}\n"
        "_____________________________________"
    )
    print(contenido_archivo)

    try:
        with open('salida.txt', 'w') as file:
            file.write(contenido_archivo)
            print("Tiquet guardado correctamente")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")








