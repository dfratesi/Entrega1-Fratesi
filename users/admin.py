from pyexpat import model
from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile

    list_display = ["user", "phone", "address", "image"]
