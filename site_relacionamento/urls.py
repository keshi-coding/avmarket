from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from meu_app.views import home, perfil, editar_perfil, tela_inicial, verificar_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Incluindo as URLs do django-allauth
    path('', tela_inicial, name='tela_inicial'),  # Rota para a tela inicial
    path('home/', home, name='home'),  # Rota para a página inicial após login
    path('perfil/', perfil, name='perfil'),  # Rota para a página de perfil
    path('perfil/editar/', editar_perfil, name='editar_perfil'),  # Página de edição do perfil
    path('verificar-email/', verificar_email, name='verificar_email'),

]

# Serve arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
