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

## Atividades de 18-01-2025 - 21:12
- Eu comecei a testar desde o cadastro de um usuario, descobri que
existem varios templates que precisam ser estilizados e padronizados
com o bootstrap que estamos usando
- Conseguimos fazer varias validacoes no frontend do cadastro de usuario
como validacoes de email, senhas e etc.
- Tambem conseguimos depois de bater muita a cabeça a estilizar a pagina da mensagem
de validacao do email que vai para o usuario logo apos ele se cadastrar.

## Previsoes para a proxima secao de trabalho
- Precisamos continuar seguindo o teste do processo de cadastro/autenticacao/login de um usuario novo 
vamos atualizando os templates que vao aparecendo fora do padrao provavelmente todos ainda usando o padrao do allauth 
que estamos usando do django.
