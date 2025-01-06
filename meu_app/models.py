from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relacionamento com o usuário
    bio = models.TextField(blank=True, null=True)  # Campo para biografia
    location = models.CharField(max_length=100, blank=True, null=True)  # Localização
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Foto de perfil

    def __str__(self):
        return f'{self.user.username} Profile'
