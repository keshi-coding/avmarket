from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm  # Certifique-se de importar o formulário criado

@login_required
def home(request):
    return render(request, 'meu_app/home.html', {'username': request.user.username})

@login_required
def perfil(request):
    # Renderiza a página de perfil com os dados do usuário logado
    return render(request, 'meu_app/perfil.html', {
        'username': request.user.username,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'profile': request.user.profile,  # Dados adicionais do perfil
    })

@login_required
def editar_perfil(request):
    profile = request.user.profile  # Recupera o perfil do usuário logado
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  # Salva as alterações no perfil
            return redirect('perfil')  # Redireciona para a página de perfil
    else:
        form = ProfileForm(instance=profile)  # Preenche o formulário com os dados atuais do perfil
    return render(request, 'meu_app/editar_perfil.html', {'form': form})
