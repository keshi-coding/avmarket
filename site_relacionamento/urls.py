from django.conf import settings  # Importa as configurações do projeto, incluindo DEBUG e URLs de mídia
from django.conf.urls.static import static  # Necessário para servir arquivos estáticos e de mídia em desenvolvimento
from django.contrib import admin  # Importa o painel de administração do Django
from django.urls import path, include  # Ferramentas para criar rotas no Django
from meu_app.views import home, perfil, editar_perfil, tela_inicial, verificar_email, lista_mensagens, listar_usuarios
# Importa as views específicas do app 'meu_app'

# Lista de URLs do projeto
urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o painel de administração
    path('accounts/', include('allauth.urls')),  # Inclui as URLs do django-allauth para login/cadastro
    path('', tela_inicial, name='tela_inicial'),  # Rota para a tela inicial
    path('home/', home, name='home'),  # Página inicial após o login
    path('perfil/', perfil, name='perfil'),  # Página de perfil do usuário
    path('perfil/editar/', editar_perfil, name='editar_perfil'),  # Página para editar o perfil do usuário
    path('verificar-email/', verificar_email, name='verificar_email'),  # Verificação se o e-mail existe no sistema
    path('mensagens/', lista_mensagens, name='lista_mensagens'),  # Rota para exibir mensagens enviadas e recebidas
    path('usuarios/', listar_usuarios, name='listar_usuarios'), # Rota para listar usuarios
    path('perfil/<str:email>/', perfil, name="perfil_outro"),
]

# Adiciona rotas para servir arquivos de mídia no ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
