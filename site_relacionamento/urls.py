from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from meu_app.views import home, perfil, editar_perfil  # Importe a view `perfil`

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Incluindo as URLs do django-allauth
    path('', home, name='home'),  # Rota para a página inicial
    path('perfil/', perfil, name='perfil'),  # Nova rota para a página de perfil
    path('perfil/editar/', editar_perfil, name='editar_perfil'), # Página de edição do perfil
]

# Serve arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)