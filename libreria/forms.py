from django import forms
from .models import Libro, Autor


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
