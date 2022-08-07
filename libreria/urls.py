from django.urls import path
from .views import (
    lista_libros,
    libro_create,
    book_detail,
    lista_autores,
    autor_create,
    autor_detail,
)

app_name = "libreria"

urlpatterns = [
    path("", lista_libros, name="book-list"),
    path("create/", libro_create, name="create"),
    path("<int:pk>/", book_detail, name="book-detail"),
    path("autores/", lista_autores, name="autores-list"),
    path("autores/create/", autor_create, name="autor-create"),
    path("autores/<int:pk>/", autor_detail, name="autor-detail"),
]
