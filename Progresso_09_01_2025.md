
### Requisitos fixos do projeto
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

--------------------------------------------------------

### Progresso do Projeto Django - Site de Relacionamento
**Data:** 08/01/2025

#### Atividades Realizadas:
1. Implementação da funcionalidade para validar o e-mail na tela de login.
   - Adicionada uma view `verificar_email` que retorna um JSON informando se o e-mail existe no banco de dados.
   - Adicionado script na página `tela_inicial.html` para verificar o e-mail ao perder o foco do campo de entrada.
   - Configurado o frontend para exibir uma mensagem ao usuário caso o e-mail não seja encontrado no sistema.

2. Correções e melhorias:
   - Ajustado o HTML e o JavaScript para garantir que o script seja executado corretamente na página.
   - Validado o funcionamento do script no navegador, verificando o console para mensagens de erro.


#### Conclusão:
A validação de e-mail foi implementada com sucesso na tela inicial, e a funcionalidade está funcionando como esperado. O script foi depurado e corrigido para atender aos requisitos.

#### Próximos Passos:
1. Testar a funcionalidade de validação de e-mail em diferentes navegadores para garantir compatibilidade.
2. Implementar mensagens visuais mais atrativas para feedback ao usuário (ex.: estilos do Bootstrap).
3. Continuar o desenvolvimento com a próxima funcionalidade planejada.

# Progresso Atualizado - 09/01/2025

## Atualizações do Projeto

### Funcionalidades Testadas e Implementadas:
1. **Sistema de Recuperação de Senha:**
   - Implementado template `password_reset.html` com design responsivo usando Bootstrap.
   - Corrigido comportamento de campos de entrada com bordas azuis ao foco, similar ao `tela_frente.html`.
   - Removido menu de navegação em telas de recuperação de senha.

2. **Correções de Erros:**
   - Ajustado problema com autenticação devido à ausência de `AUTHENTICATION_BACKENDS` no `settings.py`.
   - Configuração de `ACCOUNT_LOGIN_ATTEMPTS_LIMIT` para controle de tentativas de login inválidas.

3. **Integração de Mailtrap:**
   - Configuração do Mailtrap como servidor de e-mail padrão, substituindo o Gmail.
   - Testado com sucesso envio e recebimento de e-mails no ambiente local.

### Estrutura do Projeto Atualizada:
- Atualizada estrutura de pastas do projeto com base nos novos diretórios e arquivos.
- Implementação de `gitignore` para excluir arquivos desnecessários do versionamento.

## Próximos Passos:
1. Revisar templates para garantir consistência visual.
2. Implementar funcionalidades adicionais de perfil e sistema de "match".
3. Separar funcionalidade bilíngue para futura implementação.
