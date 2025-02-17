from django.urls import resolve

def hide_menu(request):
    """Define se o menu deve ser ocultado com base na URL."""
    excluded_urls = ['tela_inicial', 'account_signup', 'account_reset_password']
    try:
        current_url_name = resolve(request.path_info).url_name
    except:
        # Caso não consiga resolver, mantém o menu visível
        current_url_name = None
    return {'hide_menu': current_url_name in excluded_urls}
