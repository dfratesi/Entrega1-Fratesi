from django.contrib import admin
from .models import Libro, Genero, Autor, Idioma

admin.site.register(Libro)
admin.site.register(Genero)
admin.site.register(Autor)
admin.site.register(Idioma)
