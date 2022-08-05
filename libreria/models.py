from tabnanny import verbose
from unicodedata import name
from django.db import models


class Libro(models.Model):
    title = models.CharField("Título", max_length=50)
    editorial = models.CharField("Editorial", max_length=50, null=True, blank=True)
    isbn = models.CharField("ISBN", max_length=13, null=True, blank=True)
    idioma = models.ForeignKey(
        "Idioma", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title", "editorial"]


class Autor(models.Model):
    name = models.CharField("Nombre", max_length=20, null=True, blank=True)
    last_name = models.CharField("Apellido", max_length=50)

    class Meta:
        ordering = ["last_name", "name"]
        verbose_name_plural = "Autores"

    def __str__(self):
        return f"{self.last_name} {self.name}"


class Genero(models.Model):
    name = models.CharField(
        "Género",
        max_length=100,
        help_text="Ingresa un género de libro (ej. Ciencia Ficción, Misterio)",
    )


class Idioma(models.Model):
    idioma = models.CharField(max_length=50)

    def __str__(self):
        return self.idioma
