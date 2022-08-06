from os import fsdecode
from django.urls import path
from .views import lista_libros

app_name = "libreria"

urlpatterns = [
    path("libros/", lista_libros, name="book-list"),
]
