from django.urls import path
from .views import (
    libro_create,
    lista_autores,
    autor_create,
    autor_detail,
    lista_generos,
    genero_create,
    genero_detail,
    search_books,
    idioma_create,
    BookListView,
    BookDetailView,
)

app_name = "libreria"

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("create/", libro_create, name="create"),
    path("<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("search/", search_books, name="search-book"),
    path("autores/", lista_autores, name="autores-list"),
    path("autores/create/", autor_create, name="autor-create"),
    path("autores/<int:pk>/", autor_detail, name="autor-detail"),
    path("generos/", lista_generos, name="generos-list"),
    path("generos/create/", genero_create, name="genero-create"),
    path("generos/<int:pk>/", genero_detail, name="genero-detail"),
    path("idiomas/create/", idioma_create, name="idiomas-create"),
]
