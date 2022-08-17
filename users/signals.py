from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

user = get_user_model()

from .models import UserProfile


@receiver(post_save, sender=user)
def create_profile(sender, instance, created, **kwargs):
    """Crea un perfil automaticamente cuando se crea un usuario."""
    if created:
        UserProfile.objects.create(user=instance)
