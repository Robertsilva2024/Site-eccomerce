import locale
from django import template

register = template.Library()

# Configure o locale para o padrão brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

@register.filter(name='currency')
def currency(number):
    # Formata o número como moeda brasileira com vírgula
    return locale.currency(number, symbol='R$', grouping=True)

@register.filter(name='multiply')
def multiply(number, number1):
    return number * number1
