from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro, Autor, Genero
from .forms import LibroForm, AutorForm


def home(request):
    return render(request, "index.html")


def lista_libros(request):
    libros = Libro.objects.all()
    context = {"libros": libros}
    return render(request, "libreria/libro_list.html", context=context)


def libro_create(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = LibroForm()
    context = {"form": form}
    return render(request, "libreria/libro_create.html", context=context)


def book_detail(request, pk):
    """Detalle del libro"""
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, "libreria/libro_detail.html", {"libro": libro})


def lista_autores(request):
    autores = Autor.objects.all()
    context = {"autores": autores}
    return render(request, "libreria/autor_list.html", context=context)


def autor_create(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AutorForm()
    context = {"form": form}
    return render(request, "libreria/autor_create.html", context=context)


def autor_detail(request, pk):
    """Detalle del Autor"""
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, "libreria/autor_detail.html", {"autor": autor})
