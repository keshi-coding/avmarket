from allauth.account.forms import SignupForm
from allauth.account.models import EmailAddress
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Profile, Post
from groups_manager.models import Group, Member # Modelo de comunidades
from django.shortcuts import render

@login_required
def detalhes_comunidade(request, group_id):
    comunidade = get_object_or_404(Group, id=group_id)
    membros = comunidade.members
    posts = comunidade.posts.order_by('-criado_em')  # Exibe postagens mais recentes primeiro

    # Processar novo post
    if request.method == 'POST':
        conteudo = request.POST.get('conteudo')
        if conteudo:
            Post.objects.create(comunidade=comunidade, autor=request.user, conteudo=conteudo)
            messages.success(request, "Postagem criada com sucesso!")
            return redirect('detalhes_comunidade', group_id=group_id)
        else:
            messages.error(request, "O conteúdo do post não pode estar vazio.")

    return render(request, 'detalhes_comunidade.html', {
        'comunidade': comunidade,
        'membros': membros,
        'posts': posts
    })

@login_required
def entrar_comunidade(request, group_id):
    """
    Permite que o usuário entre em uma comunidade.
    """
    comunidade = get_object_or_404(Group, id=group_id)

    # Criar ou obter o membro associado ao usuário
    membro, criado = Member.objects.get_or_create(django_user=request.user)

    # Verificar se o membro já está na comunidade antes de adicionar
    if membro not in comunidade.members:
        try:
            comunidade.add_member(membro)  # Adicionar o membro à comunidade
            messages.success(request, f"Você entrou na comunidade {comunidade.name}!")
        except Exception as e:
            messages.error(request, f"Erro ao entrar na comunidade: {str(e)}")
    else:
        messages.info(request, "Você já faz parte dessa comunidade.")

    return redirect('comunidades')


@login_required
def comunidades(request):
    """
    Exibe a pagina principal das comunidades
    """
    comunidades = Group.objects.filter(parent=None) # Busca todas as comunidades
    return render(request, 'comunidades.html', {'comunidades': comunidades})

@login_required
def home(request):
    """
    Exibe a página inicial para usuários logados.
    """
    return render(request, 'home.html', {'username': request.user.username})


@login_required
def perfil(request, username=None):
    """
    Exibe o perfil do usuário logado ou de outro usuário.
    """
    user = get_object_or_404(User, username=username) if username else request.user

    return render(request, 'perfil.html', {
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
    return render(request, 'editar_perfil.html', {'form': form})


def tela_inicial(request):
    """
    Exibe a tela inicial para usuários não logados.
    """
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'tela_inicial.html')


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
def listar_usuarios(request):
    """
    Lista todos os perfis de usuários registrados, exceto o usuário logado.
    """
    usuarios = Profile.objects.exclude(user=request.user)
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

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
