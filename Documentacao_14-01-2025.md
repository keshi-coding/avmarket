## Documentação do Projeto
#### GPT este arquivo voce nao deve mexer no cabeçalho e nem nos requisitos fixos do projeto pois servirá como norte para o nosso trabalho
#### Eu acho que seria bom voce sempre adicionar o que nos fizemos colocando a data atual e descrevendo coisas importantes mas nunca apagar ou substituir atualizacoes.

## Requisitos fixos do projeto
Este cabeçalho deve ficar fixo toda vez que vc atualizar esse arquivo, você pode riscar dar um check ou riscar ou marcar como OK na frente da linha
se tivermos terminado de implementar e testado o requisito

- um site de relacionamento LGBTQ que seja como se fosse uma rede social, com fórum e sistema de match, usuários assinantes e gratuitos
- foco primeiramente em 2 línguas japonês e ingles
- usuários gratuitos podem utilizar todo o site com várias limitações como por exemplo, ver apenas um pouco do fórum para instigar a assinatura
- usuários gratuitos tem varias coisas sem acesso mas incentivar ele a assinar mensalmente
- vários campos no seu perfil e filtros para que os usuários possam procurar um ao outro
- tendo vários campos e filtros também ajuda o sistema de match automático mostrar sugestões ao usuario
- usuários podem colocar varias fotos
- sistema de verificação de cadastro, usuário gratuito pode se tornar verificado, somente verificados podem ser assinantes
- na verificação de cadastro precisamos ter regras rígidas e uma verificação para ver se ele eh realmente lgbtq
- fórum com categorias criadas apenas pelo admin, mas que permite a participação dos usuários
- sistema de mensagens com áudio gravações não precisa ser stream live
- sistema de mensagens texto com uma espécie de opção para traduzir automaticamente a janela de acordo com a língua do site ou seja de inicio japonês <> inglês
- design responsivo ou seja não vou ter APP então o acesso sera via browser mas tem que funcionar legal design e visualmente em qualquer dispositivo
- Um sistema de pontuação ou seja uplevel, terei vários níveis em que a participação do usuário no site em vários locais sera importante
  por exemplo se ele postar ou responder algo no fórum vai ganhar pontos para isso e vai acumulando no perfil dele 
  se ele completar o perfil 100% também ganha ponto
  se ele eh assinante a x tempo tbem ganha ponto
  aqui vamos implementar varias coisas que ele possa somar pontuações
- Mural pra cada um postar coisas do dia a dia e os outros tem acesso a esse mural
- Curtidas, Seguir, Adicionar na lista de amigos
- O site precisa ter um blog para artigos e noticias sobre o mundo lgbt aqui não sei como fazer por enquanto tem inglês e japonês mas qdo aumentar a língua como faremos
- preciso ter uma parte que se chama EVENTOS, onde preciso de uma interface para criar eventos online ou presenciais, com dados, informações, taxa de inscrição, endereço, fotos, vídeos
- quaisquer outras ideias e recomendações de funcionalidades e coisas legais que pode ter em um site assim do GPT também são bem vindos daqui para baixo.
- no futuro eu posso nomear um perfil para ser coordenador regional de uma cidade ou província para gerir clubes
- quero ter clubes de cada província e estado como se fosse grupos do facebook, mas serão fixos, a medida que crescer vou nomear os coordenadores no entanto se um perfil
  estiver participando de um clube, isso deve aparecer no perfil dele.
- o sistema de busca, chat, perfil e etc deve ser como no facebook.

--------------------------------------------------------
#### Daqui pra frente voce pode adicionar/alterar coisas menos apagar, sempre atualize a data caso voce edite ou adicione algo daqui para baixo:

### Estrutura das pastas
#### Ultima atualizacao: 15-01-2025

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
#### Ultima atualizacao: 15-01-2025

| **Nome da Função**    | **Responsabilidade**                                                                                | **Autenticação Necessária?**       |
|-----------------------|-----------------------------------------------------------------------------------------------------|------------------------------------|
| `home`                | Renderiza a página inicial após o login, mostrando o nome do usuário logado.                        | Sim (`@login_required`)            |
| `perfil`              | Renderiza a página de perfil do usuário, exibindo informações como nome e e-mail.                  | Sim (`@login_required`)            |
| `editar_perfil`       | Permite que o usuário edite seu perfil, salvando as alterações no banco de dados.                  | Sim (`@login_required`)            |
| `tela_inicial`        | Renderiza a tela inicial para login ou cadastro.                                                   | Não                                 |
| `verificar_email`     | Verifica se um e-mail já está cadastrado no banco de dados.                                        | Não                                 |
| `signup_view`         | View de cadastro de usuários, exibindo formulário e validando dados.                                | Não                                 |
| `lista_mensagens`     | Lista as mensagens enviadas e recebidas pelo usuário logado.                                       | Sim (`@login_required`)            |
| `listar_usuarios`     | Lista todos os perfis de usuários registrados, exceto o usuário logado.                            | Sim (`@login_required`)            |


### Templates
#### Arquivo: `urls.py`
#### Ultima atualizacao: 15-01-2025

| **Nome do Template**  | **Caminho/Arquivo**         | **Responsabilidade**                                                                                          | **Rotas**                                                          |
|-----------------------|-----------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| `tela_inicial`        | `meu_app/tela_inicial.html` | Tela inicial (login/cadastro) para usuários não logados.                                                      | `/` (name='tela_inicial')                                          |
| `home`                | `meu_app/home.html`         | Página inicial após login, mostrando o nome do usuário logado.                                               | `/home/` (name='home')                                             |
| `perfil`              | `meu_app/perfil.html`       | Exibe o perfil do usuário (nome, e-mail, etc.).                                                               | `/perfil/` (name='perfil') e `/perfil/<str:email>/` (name='perfil_outro') |
| `editar_perfil`       | `meu_app/editar_perfil.html`| Permite edição do perfil do usuário.                                                                          | `/perfil/editar/` (name='editar_perfil')                           |
| `lista_mensagens`     | `meu_app/lista_mensagens.html`| Lista as mensagens enviadas e recebidas pelo usuário logado.                                                 | `/mensagens/` (name='lista_mensagens')                             |
| `listar_usuarios`     | `meu_app/listar_usuarios.html`| Lista todos os perfis de usuários registrados, exceto o usuário logado.                                      | `/usuarios/` (name='listar_usuarios')                              |
| `signup_view`         | `account/signup.html`       | Exibe o formulário de cadastro (django-allauth).                                                              | `/accounts/signup/` (padrão do django-allauth)                     |

Obs.: A view `verificar_email` não renderiza template (retorna JSON).

### Variáveis Importantes de contexto em cada view
#### Arquivo: `views.py`
#### Ultima atualizacao: 15-01-2025

| **View**            | **Variável**             | **Descrição**                                                  | **Exemplo de Uso**                        |
|---------------------|--------------------------|----------------------------------------------------------------|-------------------------------------------|
| `home`             | `username`               | Nome de usuário logado.                                        | Exibe o nome no template `meu_app/home.html`. |
| `perfil`           | `username`               | Nome de usuário (logado ou outro, se houver `email`).          | Exibe o nome no template `meu_app/perfil.html`.|
| `perfil`           | `email`                  | E-mail do usuário.                                             | Formulários e exibição em perfil.         |
| `perfil`           | `first_name`             | Primeiro nome do usuário.                                      | Exibição no perfil.                       |
| `perfil`           | `last_name`              | Último nome do usuário.                                        | Exibição no perfil.                       |
| `perfil`           | `profile`                | Objeto `Profile` vinculado ao usuário.                         | Exibição de detalhes extras do perfil.    |
| `editar_perfil`    | `form`                   | Formulário (`ProfileForm`) para editar dados do perfil.        | Renderizado em `meu_app/editar_perfil.html`.|
| `signup_view`      | `form`                   | Formulário (`SignupForm`) para cadastro de novos usuários.     | Renderizado em `account/signup.html`.     |
| `lista_mensagens`  | `mensagens_enviadas`     | QuerySet das mensagens enviadas pelo usuário logado.           | Listagem em `meu_app/lista_mensagens.html`.|
| `lista_mensagens`  | `mensagens_recebidas`    | QuerySet das mensagens recebidas pelo usuário logado.          | Listagem em `meu_app/lista_mensagens.html`.|
| `listar_usuarios`  | `usuarios`               | QuerySet de perfis (exclui o usuário logado).                  | Listagem em `meu_app/listar_usuarios.html`.|

### Rotas (URLs)
#### Arquivo: `urls.py`
#### Ultima atualizacao: 15-01-2025

| **Rota**                | **Nome**           | **View**             | **Descrição**                                                                                    |
|-------------------------|--------------------|----------------------|---------------------------------------------------------------------------------------------------|
| `/admin/`              | *N/A*              | `admin.site.urls`    | Painel de administração do Django.                                                                |
| `/accounts/`           | *N/A*              | *Inclui django-allauth* | URLs padrão do django-allauth para autenticação e cadastro.                                        |
| `/`                    | `tela_inicial`     | `tela_inicial`       | Exibe a tela inicial para login ou cadastro.                                                      |
| `/home/`               | `home`             | `home`               | Página inicial após o login.                                                                      |
| `/perfil/`             | `perfil`           | `perfil`             | Renderiza o perfil do usuário logado.                                                             |
| `/perfil/editar/`      | `editar_perfil`    | `editar_perfil`      | Permite edição do perfil do usuário.                                                              |
| `/verificar-email/`    | `verificar_email`  | `verificar_email`    | Retorna JSON para verificar se um e-mail já está cadastrado.                                      |
| `/mensagens/`          | `lista_mensagens`  | `lista_mensagens`    | Lista mensagens enviadas e recebidas pelo usuário logado.                                         |
| `/usuarios/`           | `listar_usuarios`  | `listar_usuarios`    | Lista todos os perfis de usuários, exceto o usuário logado.                                       |
| `/perfil/<str:email>/` | `perfil_outro`     | `perfil`             | Exibe o perfil de outro usuário com base no e-mail informado.                                     |

### Outras Observações

- **Decorators Utilizados:**
  - `@login_required`: Garante que apenas usuários autenticados acessem as views `home`, `perfil`, e `editar_perfil`.

- **Redirecionamentos:**
  - Após salvar as alterações no perfil (`editar_perfil`), o usuário é redirecionado para a página de `perfil`.

- **Telas Responsivas:**
  - Todos os templates foram ajustados para usar o Bootstrap, garantindo responsividade para dispositivos móveis e desktops.

---

### Atualizações de XX/XX/XXXX
