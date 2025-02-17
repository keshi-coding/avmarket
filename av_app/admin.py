from django.contrib import admin
from .models import Profile

# Registro do modelo Profile para aparecer no painel de administração

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'age', 'country', 'city', 'marital_status')
    # Campos exibidos na lista de perfis no admin

    list_filter = ('country', 'marital_status', 'lgbtq_status')  # Filtros laterais
    search_fields = ('user__username', 'nickname', 'city', 'interests')  # Barra de busca

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('user', 'nickname', 'birth_date', 'profile_picture')
        }),
        ('Localização', {
            'fields': ('country', 'state', 'city')
        }),
        ('Relacionamento e Interesses', {
            'fields': ('marital_status', 'interests', 'profession', 'looking_for', 'age_range')
        }),
        ('Estilo de Vida', {
            'fields': ('religion', 'languages', 'smoking_status', 'drinking_status', 'more_homebody', 'less_homebody')
        }),
        ('Corpo', {
            'fields': ('body_type', 'height', 'weight')
        }),
        ('LGBTQ+', {
            'fields': ('lgbtq_status', 'relationship_role', 'role_description')
        }),
        ('Outros', {
            'fields': ('headline', 'photo_album')
        }),
    )
