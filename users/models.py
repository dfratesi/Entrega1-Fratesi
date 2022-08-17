from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(user, verbose_name="Usuario", on_delete=models.CASCADE)
    phone = models.CharField("Telefono", max_length=20, null=True, blank=True)
    address = models.CharField("Direccion", max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="profile_image/", null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} profile"

    class Meta:
        ordering = [
            "user",
        ]
        verbose_name_plural = "Perfiles"
        verbose_name = "Perfil"
