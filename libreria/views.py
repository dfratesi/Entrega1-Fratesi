from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from .models import Libro, Autor, Genero


def home(request):
    return render(request, "index.html")


def lista_libros(request):
    libros = Libro.objects.all()
    context = {"libros": libros}
    return render(request, "libreria/libros_list.html", context=context)
