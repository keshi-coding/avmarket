from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Profile


# Formulário para editar o perfil do usuário
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'nickname', 'birth_date', 'country', 'state', 'city',
            'marital_status', 'interests', 'profession', 'looking_for',
            'age_range', 'religion', 'languages', 'smoking_status',
            'drinking_status', 'more_homebody', 'less_homebody',
            'body_type', 'height', 'weight', 'lgbtq_status',
            'relationship_role', 'role_description', 'headline', 'profile_picture'
        ]


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
        # Aplica a classe 'form-control' em todos os campos automaticamente
        field.widget.attrs.update({'class': 'form-control'})


# Formulário personalizado para cadastro
class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        # Inicializa o formulário padrão do Allauth
        super().__init__(*args, **kwargs)
        # Esconde o campo de username no formulário (não será visível para o usuário)
        self.fields['username'].widget = forms.HiddenInput()
        # Define um valor temporário para o username, necessário durante o cadastro
        self.fields['username'].initial = 'temp_username'

    def clean_email(self):
        """
        Verifica se o e-mail já existe no banco de dados.
        Se existir, levanta um erro de validação.
        """
        email = self.cleaned_data['email']  # Obtém o e-mail informado pelo usuário
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este e-mail já está cadastrado. Por favor, use outro.")
        return email  # Retorna o e-mail validado

    def save(self, request):
        """
        Sobrescreve o método save para personalizar o processo de salvamento do usuário.
        - Define o username como a parte antes do "@" no e-mail.
        """
        user = super().save(request)  # Salva o usuário com os dados padrão do Allauth
        # Define o username como a parte antes do "@" no e-mail
        user.username = user.email.split('@')[0]
        user.save()  # Salva o usuário novamente com o username atualizado
        return user  # Retorna o objeto do usuário
