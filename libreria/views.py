from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from .models import Libro, Autor, Genero


def lista_libros(request):
    libros = Libro.objects.all()
    context = {"libros": libros}
    return render(request, "libreria/libros_list.html", context=context)
