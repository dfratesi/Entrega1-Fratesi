from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro, Autor, Genero
from .forms import LibroForm


def home(request):
    return render(request, "index.html")


def lista_libros(request):
    libros = Libro.objects.all()
    context = {"libros": libros}
    return render(request, "libreria/libros_list.html", context=context)


def libro_create(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = LibroForm()
    context = {"form": form}
    return render(request, "libreria/libros_create.html", context=context)
