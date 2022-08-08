from django import forms
from .models import Libro, Autor, Genero, Idioma


class LibroForm(forms.ModelForm):
    """Form para agregar y editar libros"""

    class Meta:
        model = Libro
        fields = "__all__"


class AutorForm(forms.ModelForm):
    """Form para agregar y editar autores"""

    class Meta:
        model = Autor
        fields = "__all__"


class GeneroForm(forms.ModelForm):
    """Form para agregar y editar generos literarios"""

    class Meta:
        model = Genero
        fields = "__all__"


class IdiomaForm(forms.ModelForm):
    """Form para agregar y editar idiomas"""

    class Meta:
        model = Idioma
        fields = "__all__"
