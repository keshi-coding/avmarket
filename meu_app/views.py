from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User

@login_required
def home(request):
    # Página inicial após login
    return render(request, 'meu_app/home.html', {'username': request.user.username})


@login_required
def perfil(request):
    # Página de perfil do usuário logado
    return render(request, 'meu_app/perfil.html', {
        'username': request.user.username,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'profile': request.user.profile,  # Dados adicionais do perfil
    })


@login_required
def editar_perfil(request):
    from .forms import ProfileForm  # Importação atrasada para evitar circular import

    profile = request.user.profile  # Recupera o perfil do usuário logado
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  # Salva as alterações no perfil
            return redirect('perfil')  # Redireciona para a página de perfil
    else:
        form = ProfileForm(instance=profile)  # Preenche o formulário com os dados atuais do perfil
    return render(request, 'meu_app/editar_perfil.html', {'form': form})


def tela_inicial(request):
    # Tela inicial (antes do login)
    if request.user.is_authenticated:
        return redirect('home')  # Redireciona para home se o usuário já estiver logado
    return render(request, 'meu_app/tela_inicial.html')

def verificar_email(request):
    if request.method == "GET":
        email = request.GET.get('email', None)
        if email:
            existe = User.objects.filter(email=email).exists()
            return JsonResponse({'existe': existe})
    return JsonResponse({'existe': False})
