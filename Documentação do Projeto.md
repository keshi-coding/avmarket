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

