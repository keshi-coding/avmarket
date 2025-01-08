from django import forms
from .models import Profile
from allauth.account.forms import SignupForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'profile_picture']  # Campos que o usuário pode editar
        labels = {
            'bio': 'Biografia',
            'location': 'Localização',
            'profile_picture': 'Foto de Perfil',
        }

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Esconde o campo de username no formulário
        self.fields['username'].widget = forms.HiddenInput()
        self.fields['username'].initial = 'temp_username'  # Define um valor temporário

    def save(self, request):
        # Salva o usuário com o username baseado no e-mail
        user = super().save(request)
        user.username = user.email.split('@')[0]  # Define o username como parte antes do "@"
        user.save()
        return user
