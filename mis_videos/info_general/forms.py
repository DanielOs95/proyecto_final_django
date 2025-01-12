from django import forms
from .models import Usuario, Video

#aqui se crean las instancias pra el formulario que obtendra los datos del usuario id_nomina y nombre_usuario
#tambien se hacen las validaciones para los inputs
class UsuarioForm(forms.ModelForm):
    video = forms.IntegerField()
    class Meta:
        model = Usuario
        fields = ['id_nomina', 'nombre_usuario', 'video']
    def clean_id_nomina(self):
        id_nomina = self.cleaned_data.get('id_nomina')
        if not id_nomina.replace(" ", "").isalnum():
            raise forms.ValidationError("Formato incorrecto, ingrese solo numeros y letras")
        return id_nomina

    def clean_nombre_usuario(self):
        nombre_usuario = self.cleaned_data.get('nombre_usuario')
        if not nombre_usuario.replace(" ", "").isalpha():
            raise forms.ValidationError("Formato incorrecto, ingrese solo letras")
        return nombre_usuario


#aqui se crean las instancias para el formulario que obtendra los datos de los videos nombre_video, extension_video y tamano_video
#tambien se hacen las validaciones para los inputs de los videos
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['nombre_video', 'extension_video', 'tamano_video']

    def clean_nombre_video(self):
        nombre_video = self.cleaned_data.get('nombre_video')
        if not nombre_video.replace(" ", "").isalnum():
            raise forms.ValidationError("Nombre en formato incorrecto, ingrese solo numeros y letras")
        return nombre_video

    def clean_extension_video(self):
        extension_video = self.cleaned_data.get('extension_video')
        extensiones = [".mp4", ".avi", ".mov", ".wmv", ".mkv", ".webm", ".flv", ".mpg"]
        if extension_video not in extensiones:
            raise forms.ValidationError("Extension en formato incorrecto, ingrese solo extensiones validas")
        return extension_video

    def clean_tamano_video(self):
        tamano_video = self.cleaned_data.get('tamano_video')
        if not(0 < tamano_video <= 3):
            raise forms.ValidationError("El archivo no debe pesar mas de 3 MB")
        return tamano_video


