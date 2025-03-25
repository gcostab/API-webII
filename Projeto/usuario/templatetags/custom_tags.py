from django import template
from usuario.models import Usuario  # Importar o modelo correto

register = template.Library()

@register.filter
def get_size_items(user):
    if isinstance(user, Usuario):
        return f"{user.get_size_items()}"
    return "0"
