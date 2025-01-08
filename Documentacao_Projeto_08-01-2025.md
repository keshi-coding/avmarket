
# Documentação do Projeto

## Variáveis Importantes
- **BASE_DIR**: Define o diretório base do projeto Django.
- **EMAIL_HOST_USER**: 'keshi.coding@gmail.com' - Email utilizado para envio de mensagens.
- **EMAIL_HOST_PASSWORD**: Senha específica do aplicativo para o envio de e-mails.
- **LOGIN_REDIRECT_URL**: '/' - Redireciona para a página inicial após login.
- **DATABASES**: Configuração do banco de dados PostgreSQL local.

## Estrutura de Arquivos
```
site-relacionamento/
├── media/
│   └── profile_pictures/
├── meu_app/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── meu_app/
│   │       ├── tela_inicial.html
│   │       ├── editar_perfil.html
│   │       ├── signup.html
│   │       └── perfil.html
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── site_relacionamento/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

## Scripts e Códigos Importantes
### Validação de E-mail no Front-End
Adicionado no arquivo `tela_inicial.html`:
```html
<script>
    document.addEventListener("DOMContentLoaded", function () {
        const emailField = document.querySelector("#id_email");
        const emailFeedback = document.querySelector("#email_feedback");

        emailField.addEventListener("blur", function () {
            const email = emailField.value.trim();

            if (email.length > 3) {
                fetch(`/verificar-email/?email=${encodeURIComponent(email)}`)
                    .then(response => response.json())
                    .then(data => {
                        if (!data.existe) {
                            emailFeedback.textContent = "E-mail não encontrado. Você pode se cadastrar.";
                        } else {
                            emailFeedback.textContent = "";
                        }
                    })
                    .catch(error => {
                        console.error("Erro ao verificar o e-mail:", error);
                        emailFeedback.textContent = "Erro ao verificar o e-mail. Tente novamente mais tarde.";
                    });
            } else {
                emailFeedback.textContent = "";
            }
        });
    });
</script>
```

---
Última Atualização: 08/01/2025 13:33
