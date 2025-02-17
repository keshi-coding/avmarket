from django.contrib.auth.models import User
from av_app.models import Profile  # Substitua 'core' pelo nome correto do seu app
import random

cidades = ["Tóquio", "São Paulo", "Nova York", "Londres", "Paris", "Berlim", "Seul", "Toronto", "Barcelona", "Sydney"]

for i, letra in enumerate("abcdefghij"):
    username = f"fulano_{letra}"
    email = f"{username}@teste.com"
    senha = f"Fulano{letra.upper()}142"

    # Criar usuário apenas se ainda não existir
    user, created = User.objects.get_or_create(username=username, email=email)
    if created:
        user.set_password(senha)
        user.is_active = True
        user.save()
        print(f"Usuário {username} criado com sucesso!")
    else:
        print(f"Usuário {username} já existe, pulando...")

    # Criar perfil apenas se ainda não existir
    if not Profile.objects.filter(user=user).exists():
        Profile.objects.create(
            user=user,
            nickname=username,
            birth_date="1990-01-01",
            country="Japão",
            state="Tóquio",
            city=random.choice(cidades),
            marital_status="Solteiro",
            interests="Música, Filmes, Tecnologia",
            profession="Engenheiro",
            looking_for="Amizade",
            age_range="25-35",
            religion="Agnóstico",
            languages="Japonês, Inglês",
            smoking_status="Não",
            drinking_status="Sim",
            body_type="Magro",
            height=random.randint(160, 190),
            weight=random.randint(50, 90),
            lgbtq_status="Sim, para todos",
            relationship_role="Versátil",
            headline="Buscando novas amizades!"
        )
        print(f"Perfil de {username} criado com sucesso!")
    else:
        print(f"Perfil de {username} já existe, pulando...")

print("Criação de usuários e perfis concluída!")
