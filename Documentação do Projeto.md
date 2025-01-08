## Documentação do Projeto

### Views

#### Arquivo: `views.py`

| **Nome da Função**   | **Responsabilidade**                                                                 | **Autenticação Necessária?** |
|-----------------------|--------------------------------------------------------------------------------------|------------------------------|
| `home`               | Renderiza a página inicial após o login, mostrando o nome do usuário logado.         | Sim (`@login_required`)      |
| `perfil`             | Renderiza a página de perfil do usuário, exibindo informações como nome e e-mail.    | Sim (`@login_required`)      |
| `editar_perfil`      | Permite que o usuário edite seu perfil, salvando as alterações no banco de dados.     | Sim (`@login_required`)      |
| `tela_inicial`       | Renderiza a tela inicial para login ou cadastro.                                      | Não                          |

---

### Templates

#### Utilizados pelas Views

| **Nome do Template**           | **Função Associada**    | **Descrição**                                 |
|--------------------------------|-------------------------|-----------------------------------------------|
| `meu_app/home.html`            | `home`                 | Página inicial após o login.                  |
| `meu_app/perfil.html`          | `perfil`               | Exibe os detalhes do perfil do usuário.       |
| `meu_app/editar_perfil.html`   | `editar_perfil`        | Formulário para edição do perfil do usuário.  |
| `meu_app/tela_inicial.html`    | `tela_inicial`         | Tela inicial para login ou cadastro.          |

---

### Variáveis Importantes no Contexto

| **Nome da Variável** | **Função Associada** | **Descrição**                                           |
|-----------------------|----------------------|---------------------------------------------------------|
| `username`           | `home`, `perfil`    | Armazena o nome de usuário logado.                     |
| `email`              | `perfil`            | E-mail do usuário logado.                              |
| `first_name`         | `perfil`            | Primeiro nome do usuário logado.                       |
| `last_name`          | `perfil`            | Sobrenome do usuário logado.                           |
| `profile`            | `perfil`, `editar_perfil` | Dados adicionais do perfil do usuário logado.         |
| `form`               | `editar_perfil`     | Instância do formulário para edição do perfil.         |

---
## Rotas (URLs)
### Arquivo: `urls.py`

| **URL**                | **View Associada**   | **Descrição**                                      |
|------------------------|----------------------|--------------------------------------------------|
| `/admin/`              | -                   | Acesso ao painel de administração do Django.      |
| `/accounts/`           | Inclui URLs padrão  | Rotas do `django-allauth` para login/cadastro.    |
| `/`                    | `tela_inicial`      | Tela inicial para login/cadastro.                |
| `/home/`               | `home`              | Página inicial após o login do usuário.          |
| `/perfil/`             | `perfil`            | Exibe as informações do perfil do usuário.       |
| `/perfil/editar/`      | `editar_perfil`     | Permite edição do perfil do usuário.             |


### Outras Observações

- **Decorators Utilizados:**
  - `@login_required`: Garante que apenas usuários autenticados acessem as views `home`, `perfil`, e `editar_perfil`.

- **Redirecionamentos:**
  - Após salvar as alterações no perfil (`editar_perfil`), o usuário é redirecionado para a página de `perfil`.

- **Telas Responsivas:**
  - Todos os templates foram ajustados para usar o Bootstrap, garantindo responsividade para dispositivos móveis e desktops.

---

Essa é a documentação inicial das Views e Templates. Atualize conforme necessário para manter tudo alinhado e claro.


## Atualizações de 08/01/2025

### Templates
- **tela_inicial.html**:
  - Script de validação para verificar se o e-mail já existe no banco de dados:
    ```javascript
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
                                emailFeedback.textContent = ""; // Limpa a mensagem se o e-mail existir
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
  - Campo de e-mail ajustado com `id_email` e feedback dinâmico de validação.

### Novas Rotas
- **/verificar-email/**:
  - Endpoint criado para verificar se o e-mail existe no banco de dados.
  - Retorna um JSON com `{ "existe": true }` ou `{ "existe": false }`.

### Outros
- Confirmado que a configuração `ACCOUNT_SIGNUP_FORM_CLASS` no `settings.py` foi removida sem impacto, pois não estamos alterando o comportamento interno do `allauth`, apenas ajustando o front-end.
