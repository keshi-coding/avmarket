from django.contrib.auth.models import User  # Importa o modelo User, que gerencia usuários no Django.
from django.db import models  # Importa os utilitários para criar modelos no Django.
from groups_manager.models import Group

# Armazenar postagens feitas pelos membros
class Post(models.Model):
    comunidade = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='posts')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post de {self.autor.username} na comunidade {self.comunidade.name}"

# Modelo de Perfil para estender as informações do usuário padrão
class Profile(models.Model):
    # Relacionamento com o usuário padrão do Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Informações Básicas
    nickname = models.CharField(max_length=50, blank=False)  # Apelido
    birth_date = models.DateField(blank=False, null=True)  # Data de nascimento
    # País, Estado e Cidade
    country = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)

    # Relacionamento e Interesses
    marital_status = models.CharField(
        max_length=50,
        choices=[('Solteiro', 'Solteiro'), ('Casado', 'Casado'), ('Divorciado', 'Divorciado')],
        blank=True
    )
    interests = models.TextField(blank=True)  # Interesses/Hobbies
    profession = models.CharField(max_length=100, blank=True)  # Área de Trabalho
    looking_for = models.CharField(
        max_length=50,
        choices=[
            ('Relacionamento sério', 'Relacionamento sério'),
            ('Amizade', 'Amizade'),
            ('Algo casual', 'Algo casual')
        ],
        blank=True
    )
    age_range = models.CharField(max_length=20, blank=True)  # Faixa etária de interesse

    # Estilo de Vida
    religion = models.CharField(max_length=50, blank=True)
    languages = models.CharField(max_length=100, blank=True)
    smoking_status = models.CharField(
        max_length=50,
        choices=[('Sim', 'Sim'), ('Não', 'Não')],
        blank=True
    )
    drinking_status = models.CharField(
        max_length=50,
        choices=[('Sim', 'Sim'), ('Não', 'Não')],
        blank=True
    )
    more_homebody = models.BooleanField(default=False)  # Mais caseiro
    less_homebody = models.BooleanField(default=False)  # Menos caseiro

    # Corpo
    body_type = models.CharField(
        max_length=50,
        choices=[
            ('Magro', 'Magro'),
            ('Musculoso', 'Musculoso'),
            ('Cheinho', 'Cheinho'),
            ('Plus Size', 'Plus Size')
        ],
        blank=True
    )
    height = models.PositiveIntegerField(blank=True, null=True)  # Altura (em cm)
    weight = models.PositiveIntegerField(blank=True, null=True)  # Peso (em kg)

    # Visual
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Foto de perfil
    photo_album = models.ImageField(upload_to='photo_albums/', blank=True, null=True)  # Álbum de fotos

    # Identidade e Papel
    lgbtq_status = models.CharField(
        max_length=50,
        choices=[
            ('Sim, para todos', 'Sim, para todos'),
            ('Apenas para amigos', 'Apenas para amigos'),
            ('Não estou pronto', 'Não estou pronto')
        ],
        blank=True
    )
    relationship_role = models.CharField(
        max_length=50,
        choices=[
            ('Dominante', 'Dominante'),
            ('Submisso', 'Submisso'),
            ('Versátil', 'Versátil')
        ],
        blank=True
    )
    role_description = models.TextField(blank=True)  # Campo aberto para descrição

    # Outros
    headline = models.CharField(max_length=150, blank=True)  # Frase de destaque

    def __str__(self):
        return f'{self.user.username} Profile'
    # Define a representação em string do objeto Profile, exibindo o nome de usuário associado.

    # Função para calcular a idade com base na data de nascimento
    @property
    def age(self):
        from datetime import date
        if self.birth_date:
            today = date.today()
            return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return None


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

