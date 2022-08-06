from os import fsdecode
from django.urls import path
from .views import lista_libros, libro_create

app_name = "libreria"

urlpatterns = [
    path("", lista_libros, name="book-list"),
    path("create/", libro_create, name="create"),
]
