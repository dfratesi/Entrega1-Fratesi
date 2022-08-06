from os import fsdecode
from django.urls import path
from .views import lista_libros

app_name = "libreria"

urlpatterns = [
    path('', lista_libros, name='libro-list'),
]
