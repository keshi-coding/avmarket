from django.shortcuts import get_object_or_404, render, redirect  # Funções para renderizar templates e redirecionar URLs
from django.contrib.auth.decorators import login_required  # Decorador para restringir acesso a usuários autenticados
from django.http import JsonResponse  # Classe para retornar respostas JSON
from django.contrib.auth.models import User  # Modelo padrão de usuário do Django
from django.contrib import messages  # Para exibir mensagens
from allauth.account.forms import SignupForm  # Formulário de cadastro do django-allauth
from .models import Mensagem, Profile  # Modelos de mensagens e perfis

@login_required
def home(request):
    """
    Exibe a página inicial para usuários logados.
    """
    return render(request, 'meu_app/home.html', {'username': request.user.username})


@login_required
def perfil(request, email=None):
    """
    Exibe o perfil do usuário logado ou de outro usuário.
    - Se 'email' for fornecido, exibe o perfil do usuário correspondente.
    - Caso contrário, exibe o perfil do usuário logado.
    """
    if email:
        # Obtém o perfil do usuário com base no e-mail fornecido
        user = get_object_or_404(User, email=email)
    else:
        # Exibe o perfil do usuário logado
        user = request.user

    return render(request, 'meu_app/perfil.html', {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'profile': user.profile,
    })


@login_required
def editar_perfil(request):
    """
    Permite que o usuário edite seu perfil.
    """
    from .forms import ProfileForm  # Importação atrasada para evitar circular import

    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'meu_app/editar_perfil.html', {'form': form})


def tela_inicial(request):
    """
    Exibe a tela inicial para usuários não logados.
    """
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'meu_app/tela_inicial.html')


def verificar_email(request):
    """
    Verifica se um e-mail já está cadastrado no banco de dados.
    """
    if request.method == "GET":
        email = request.GET.get('email', None)
        if email:
            existe = User.objects.filter(email=email).exists()
            return JsonResponse({'existe': existe})
    return JsonResponse({'existe': False})


def signup_view(request):
    """
    View personalizada para cadastro de usuários.
    """
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            messages.success(request, "Cadastro realizado com sucesso! Um e-mail foi enviado para confirmação.")
            return redirect('tela_inicial')
        else:
            messages.error(request, "Erro ao tentar cadastrar. Verifique os campos e tente novamente.")
    else:
        form = SignupForm()

    return render(request, 'account/signup.html', {'form': form})


@login_required
def lista_mensagens(request):
    """
    Lista as mensagens enviadas e recebidas pelo usuário logado.
    """
    mensagens_enviadas = Mensagem.objects.filter(remetente=request.user).order_by('-timestamp')
    mensagens_recebidas = Mensagem.objects.filter(destinatario=request.user).order_by('-timestamp')

    return render(request, 'meu_app/lista_mensagens.html', {
        'mensagens_enviadas': mensagens_enviadas,
        'mensagens_recebidas': mensagens_recebidas,
    })


@login_required
def listar_usuarios(request):
    """
    Lista todos os perfis de usuários registrados, exceto o usuário logado.
    """
    usuarios = Profile.objects.exclude(user=request.user)
    return render(request, 'meu_app/listar_usuarios.html', {'usuarios': usuarios})
