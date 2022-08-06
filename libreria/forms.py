from django import forms
from .models import Libro


class LibroForm(forms.ModelForm):
    """Form para agrgar y editar libros"""

    class Meta:
        model = Libro
        fields = "__all__"
