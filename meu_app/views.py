from allauth.account.forms import SignupForm
from allauth.account.models import EmailAddress
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Mensagem, Profile


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
    """
    user = get_object_or_404(User, email=email) if email else request.user

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
    from .forms import ProfileForm

    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
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
        existe = User.objects.filter(email=email).exists() if email else False
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


@login_required
def enviar_mensagem(request, email):
    """
    Permite que o usuário logado envie uma mensagem para outro usuário.
    """
    destinatario = get_object_or_404(User, email=email)

    if request.method == 'POST':
        conteudo = request.POST.get('mensagem')
        if conteudo:
            Mensagem.objects.create(remetente=request.user, destinatario=destinatario, conteudo=conteudo)
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('perfil_outro', email=email)

    return render(request, 'meu_app/enviar_mensagem.html', {'destinatario': destinatario})


@login_required
def resend_verification_email(request):
    """
    Reenvia o e-mail de verificação para o usuário.
    """
    try:
        email_address = EmailAddress.objects.get(user=request.user, primary=True)
        if not email_address.verified:
            email_address.send_confirmation(request)
            messages.success(request, "E-mail de verificação reenviado com sucesso!")
        else:
            messages.info(request, "Este e-mail já foi verificado.")
    except EmailAddress.DoesNotExist:
        messages.error(request, "Nenhum e-mail encontrado para este usuário.")

    return redirect('account_email_verification_sent')
