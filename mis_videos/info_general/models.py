from django.db import models

class Usuario(models.Model):
    id_nomina = models.CharField(max_length=10, primary_key=True)
    nombre_usuario = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id_nomina} - {self.nombre_usuario}"

class Video(models.Model):
    nombre_video = models.CharField(max_length = 50)
    extension_video = models.CharField(max_length = 5)
    tamano_video = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_video}"

class UsuarioVideo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return f"Usuario: {self.usuario.id_nomina}, Video: {self.video.nombre_video}"