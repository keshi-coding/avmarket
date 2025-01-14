from django.contrib.auth.models import User  # Importa o modelo User, que gerencia usuários no Django.
from django.db import models  # Importa os utilitários para criar modelos no Django.

# Modelo de Perfil para estender as informações do usuário padrão
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Relacionamento um-para-um com o modelo User. Quando o usuário é deletado, o perfil também é.

    bio = models.TextField(blank=True, null=True)
    # Campo opcional para a biografia do usuário.

    location = models.CharField(max_length=100, blank=True, null=True)
    # Campo opcional para armazenar a localização do usuário, com um limite de 100 caracteres.

    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    # Campo para upload da foto de perfil do usuário. As imagens são salvas no diretório `media/profile_pictures/`.

    def __str__(self):
        return f'{self.user.username} Profile'
    # Define a representação em string do objeto Profile, exibindo o nome de usuário associado.

# Modelo de Mensagens para armazenar conversas entre usuários
class Mensagem(models.Model):
    remetente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens_enviadas')
    # Relaciona a mensagem ao remetente. `related_name` permite acessar as mensagens enviadas via `user.mensagens_enviadas`.

    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens_recebidas')
    # Relaciona a mensagem ao destinatário. `related_name` permite acessar as mensagens recebidas via `user.mensagens_recebidas`.

    conteudo = models.TextField()
    # Armazena o conteúdo da mensagem.

    timestamp = models.DateTimeField(auto_now_add=True)
    # Registra automaticamente a data e hora em que a mensagem foi criada.

    lido = models.BooleanField(default=False)
    # Indica se a mensagem foi lida pelo destinatário. Por padrão, é definida como `False`.

    def __str__(self):
        return f"Mensagem de {self.remetente} para {self.destinatario} - {self.timestamp}"
    # Define a representação em string do objeto Mensagem, exibindo o remetente, destinatário e data/hora.

