from django.conf import settings  # Importa as configurações do projeto, incluindo DEBUG e URLs de mídia
from django.conf.urls.static import static  # Necessário para servir arquivos estáticos e de mídia em desenvolvimento
from django.contrib import admin  # Importa o painel de administração do Django
from django.urls import path, include  # Ferramentas para criar rotas no Django

from av_app import views  # Importa todas as views do app principal
from av_app.views import (
    home, perfil, editar_perfil, tela_inicial, verificar_email, lista_mensagens, listar_usuarios,
    resend_verification_email, comunidades, entrar_comunidade, detalhes_comunidade
)

urlpatterns = [
    # Painel de administração do Django
    path('admin/', admin.site.urls),

    # URLs do django-allauth (login, logout, cadastro, etc.)
    path('accounts/', include('allauth.urls')),

    # Página inicial do site
    path('', tela_inicial, name='tela_inicial'),

    # Página principal após login
    path('home/', home, name='home'),

    # Página de perfil (do usuário logado ou de outro usuário)
    path('perfil/', perfil, name='perfil'),  # Perfil do próprio usuário logado
    path('perfil/<str:username>/', perfil, name="perfil_outro"),  # Perfil de outro usuário, agora por username

    # Editar perfil do usuário logado
    path('perfil/editar/', editar_perfil, name='editar_perfil'),

    # Verificação se um e-mail já existe no sistema
    path('verificar-email/', verificar_email, name='verificar_email'),

    # Listagem de mensagens enviadas e recebidas
    path('mensagens/', lista_mensagens, name='lista_mensagens'),

    # Lista de usuários cadastrados
    path('usuarios/', listar_usuarios, name='listar_usuarios'),

    # Reenvio do e-mail de verificação
    path('accounts/resend-verification-email/', resend_verification_email, name='account_resend_email'),

    # Sistema de comunidades
    path('comunidades/', comunidades, name='comunidades'),
    path('comunidades/entrar/<int:group_id>/', entrar_comunidade, name='entrar_comunidade'),
    path('comunidades/<int:group_id>/', detalhes_comunidade, name='detalhes_comunidade'),

    # Chat entre usuários (agora usando o username real do banco)
    path('chat/<str:username>/', views.chat_view, name='chat'),
]

# Servir arquivos de mídia e estáticos no ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
