from django.db import models


class Libro(models.Model):
    title = models.CharField("Título", max_length=50)
    editorial = models.CharField("Editorial", max_length=50, null=True, blank=True)
    isbn = models.CharField("ISBN", max_length=13, null=True, blank=True)
    price = models.FloatField("Precio")
    idioma = models.ForeignKey(
        "Idioma", on_delete=models.SET_NULL, null=True, blank=True
    )
    genero = models.ManyToManyField("Genero", verbose_name="Género")
    autor = models.ForeignKey(
        "Autor",
        verbose_name="Autor",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    resumen = models.TextField("Resumen", max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title", "editorial"]


class Autor(models.Model):
    name = models.CharField("Nombre", max_length=20, null=True, blank=True)
    last_name = models.CharField("Apellido", max_length=50)
    nacionalidad = models.CharField("Nacionalidad", max_length=50, null=True, blank=True)

    class Meta:
        ordering = ["last_name", "name"]
        verbose_name_plural = "Autores"

    def fullname(self):
        return f"{self.last_name} {self.name}"

    def __str__(self):
        return self.fullname()


class Genero(models.Model):
    name = models.CharField(
        "Género",
        max_length=100,
        help_text="Ingresa un género de libro (ej. Ciencia Ficción, Misterio)",
    )

    def __str__(self):
        return self.name
    


class Idioma(models.Model):
    idioma = models.CharField(max_length=50)

    def __str__(self):
        return self.idioma
