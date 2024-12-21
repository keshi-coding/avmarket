from django.contrib import admin
from .models import Profile

# Registro do modelo Profile para aparecer no painel de administração
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'bio')  # Campos que serão exibidos na lista
