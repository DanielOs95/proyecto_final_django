from django.db import models
#from pyarrow import nulls
# Create your models here.

class Usuario(models.Model):
    id_nomina = models.CharField(max_length=10, primary_key=True)
    nombre_usuario = models.CharField(max_length=50)

class Video(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="videos", null=True)
    nombre_video = models.CharField(max_length = 50)
    extension_video = models.CharField(max_length = 5)
    tamano_video = models.IntegerField()

class UsuarioVideo(models.Model):
    id_nomina = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_video = models.ForeignKey(Video, on_delete=models.CASCADE)