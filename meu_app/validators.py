import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def validate(self, password, user=None):
        # Verifica se a senha tem pelo menos 8 caracteres
        if len(password) < 8:
            raise ValidationError(
                _("A senha deve ter pelo menos 8 caracteres."),
                code='password_too_short',
            )

        # Verifica se a senha contém pelo menos uma letra (ocidental)
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                _("A senha deve conter pelo menos uma letra."),
                code='password_no_letter',
            )

        # Verifica se a senha contém pelo menos um número
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                _("A senha deve conter pelo menos um número."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Sua senha deve ter pelo menos 8 caracteres, incluindo pelo menos uma letra e um número."
        )
