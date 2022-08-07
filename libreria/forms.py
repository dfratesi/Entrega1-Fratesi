from django import forms
from .models import Libro, Autor, Genero


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
    """Form para agregar y editar autores"""

    class Meta:
        model = Genero
        fields = "__all__"
