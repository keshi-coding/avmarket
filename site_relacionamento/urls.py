from django.contrib import admin
from django.urls import path, include
from meu_app.views import home  # Certifique-se de importar a view do app correto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Incluindo as URLs do django-allauth
    path('', home, name='home'),  # Rota para a página inicial
]
