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

#### As estruturas das pastas e arquivos estao no arquivo codigos_data.md entao consulte tambem este arquivo 
#### Aqui vai ficar apenas os progressos e um breve historico do que foi feito e do que pretendemos fazer

--------------------------------------------------------

### Ferramentas que estamos utilizando
- Django Python para fazer este projeto
- Bootstrap para economizar tempo no design
- Conectado com o github
- Utilizando 2 arquivos para documentar tudo e para
facilitar a sua memoria e o cross de arquivos/variaveis e metodos
os dois arquivos sao: 
codigos_<data atual>.md / 
progresso_<data atual>.md

--------------------------------------------------------

### Instrucoes de Métodos de resposta para o CHATGPT.
- Nunca se esqueça de sempre sugerir modulos, libs prontas para facilitar a implantação quando eu peço
funcionalidades e sempre priorizar coisas prontas para economizar o tempo.
- Sempre que voce for me enviar respostas ou solucoes codigos e passos, nao envie uma lista de passos de uma só vez. 
Mas prefiro que mande 1 passo de cada vez e só seguir a sequencia quando conseguirmos 
implantar o passo 1 e eu der o OK entao podemos ir para o passo 2.
Por exemplo: 1. Faça X, 2. Faça Y, 3. Faça Z, assim tudo de uma vez fica ruim e podemos nos perder
ao invés disso quero assim por exemplo: 1. Faca X vou aguardar voce fazer 
entao eu vou tentar implantar o que vc disse se tivermos problemas vamos resolvendo
soh depois que combinarmos OK! encerramos o passo 1 e fizemos X, entao voce pode seguir para o 
Passo 2. Faca Y e assim por diante.
- Em outras palavras procure quebrar a lista de passos para nao ficarmos perdido um com o outro.

--------------------------------------------------------

## Atividades de 18-01-2025 - 21:12
- Eu comecei a testar desde o cadastro de um usuario, descobri que
existem varios templates que precisam ser estilizados e padronizados
com o bootstrap que estamos usando
- Conseguimos fazer varias validacoes no frontend do cadastro de usuario
como validacoes de email, senhas e etc.
- Tambem conseguimos depois de bater muita a cabeça a estilizar a pagina da mensagem
de validacao do email padrao do allauth que vai para o usuario logo apos ele se cadastrar.

## Atividades de 20-01-2025 - 22:50
- Adicionamos varios campos no perfil do usuario, acertamos o design deixamos
padronizado com o restante do layout os campos de input e etc. 

## Atividades de 21-01-2025 - 22:00
- Usamos o django-groups e instalamos, configuramos ja temos uma especie de comunidade
eh claro que precisa ser melhorado, mas ja esta funcionando a lista de membros e postagens.
- Demos inicio na implantacao e configuracao de chat online entre os usuarios
com o django-channels e redis...ja instalamos o channels -redis no pip
- Instalei o docker desktop com sucesso, fizemos login e demos o comando
"docker ps" no terminal do pycharm e ele mostrou que o container Redis esta funcionando e mapeado
na minha maquina na porta 6379.
 
## Previsoes para a proxima secao de trabalho
- como o container redis ja esta mapeado e funcionando na porta 6379 da minha maquina
temos que seguir para a integracao do django channels com o redis, conforme voce pode
verificar no arquivo de codigos, ja criei o arquivo asgi.py, ja mexi no settings e etc.
- precisamos seguir daqui em diante.