from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'profile_picture']  # Campos que o usuário pode editar
        labels = {
            'bio': 'Biografia',
            'location': 'Localização',
            'profile_picture': 'Foto de Perfil',
        }

