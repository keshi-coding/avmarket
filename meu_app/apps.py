from django.apps import AppConfig

class MeuAppConfig(AppConfig):
    # Define o tipo de chave primária padrão para os modelos do app
    default_auto_field = 'django.db.models.BigAutoField'

    # Nome do app (usado pelo Django para identificar este módulo)
    name = 'meu_app'

    def ready(self):
        # Importa o arquivo `signals.py` quando o app estiver pronto
        # Isso garante que os sinais sejam registrados no momento certo
        import meu_app.signals
