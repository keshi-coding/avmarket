
## Documentação do Projeto

### Estrutura das pastas

```plaintext
├── site-relacionamento/
│   ├── media/
│   │   └── profile_pictures/
│   │       ├── 995334cf347e7572e9f844ccd23d9eb1.jpg
│   │       └── ninja_forex.jpg
│   ├── meu_app/
│   │   ├── migrations/
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── static/
│   │   │   ├── css/
│   │   │   │   └── bootstrap.min.css
│   │   │   ├── js/
│   │   │   │   └── bootstrap.bundle.min.js
│   │   │   ├── images/
│   │   │   │   └── default-profile.webp
│   │   ├── templates/
│   │   │   ├── account/
│   │   │   │   ├── password_reset.html
│   │   │   │   └── signup.html
│   │   │   ├── meu_app/
│   │   │   │   ├── base.html
│   │   │   │   ├── editar_perfil.html
│   │   │   │   ├── home.html
│   │   │   │   ├── perfil.html
│   │   │   │   └── tela_inicial.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── signals.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── site_relacionamento/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── .gitignore
│   ├── dados importantes.txt
│   ├── Documentação do Projeto.md
│   ├── estrutura.txt
│   ├── manage.py
│   ├── Progresso_Atualizado_08_01_2025.md
│   └── README.md
```

### Views

#### Arquivo: `views.py`

| **Nome da Função**   | **Responsabilidade**                                                                 | **Autenticação Necessária?** |
|-----------------------|--------------------------------------------------------------------------------------|------------------------------|
| `home`               | Renderiza a página inicial após o login, mostrando o nome do usuário logado.         | Sim (`@login_required`)      |
| `perfil`             | Renderiza a página de perfil do usuário, exibindo informações como nome e e-mail.    | Sim (`@login_required`)      |
| `editar_perfil`      | Permite que o usuário edite seu perfil, salvando as alterações no banco de dados.     | Sim (`@login_required`)      |
| `tela_inicial`       | Renderiza a tela inicial para login ou cadastro.                                      | Não                          |

### Templates

#### Utilizados pelas Views

| **Nome do Template**           | **Função Associada**    | **Descrição**                                 |
|--------------------------------|-------------------------|-----------------------------------------------|
| `meu_app/home.html`            | `home`                 | Página inicial após o login.                  |
| `meu_app/perfil.html`          | `perfil`               | Exibe os detalhes do perfil do usuário.       |
| `meu_app/editar_perfil.html`   | `editar_perfil`        | Formulário para edição do perfil do usuário.  |
| `meu_app/tela_inicial.html`    | `tela_inicial`         | Tela inicial para login ou cadastro.          |

### Variáveis Importantes no Contexto

| **Nome da Variável** | **Função Associada** | **Descrição**                                           |
|-----------------------|----------------------|---------------------------------------------------------|
| `username`           | `home`, `perfil`    | Armazena o nome de usuário logado.                     |
| `email`              | `perfil`            | E-mail do usuário logado.                              |
| `first_name`         | `perfil`            | Primeiro nome do usuário logado.                       |
| `last_name`          | `perfil`            | Sobrenome do usuário logado.                           |
| `profile`            | `perfil`, `editar_perfil` | Dados adicionais do perfil do usuário logado.         |
| `form`               | `editar_perfil`     | Instância do formulário para edição do perfil.         |

### Rotas (URLs)
#### Arquivo: `urls.py`

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

## Atualizações de 14/01/2025

### Funcionalidades Testadas e Implementadas:
1. **Sistema de Visualização de Usuários**:
   - Adicionada a página `/usuarios/` para listar todos os usuários, exceto o logado.
   - Cada usuário na lista tem a opção de clicar em "Ver Perfil", que redireciona para o perfil baseado no e-mail.
   - Implementação de visualização do perfil, permitindo acesso via e-mail, não nome de usuário.

2. **Sistema de Mensagens**:
   - Implementada a funcionalidade de envio e visualização de mensagens entre usuários.
   - As mensagens são associadas ao perfil e podem ser visualizadas nas páginas de mensagens.

3. **Correção de Erro de Exibição de Perfil**:
   - Corrigido erro ao exibir o perfil de outro usuário, agora utilizando o e-mail do usuário para consulta.

### Estrutura do Projeto Atualizada:
- Atualizada a estrutura de pastas do projeto com base nos novos diretórios e arquivos, incluindo a pasta `images/` para armazenar a imagem padrão `default-profile.webp`.

---
