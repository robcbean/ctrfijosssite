from controlfitos.models import CabSalida
from datetime import datetime

from django import template
register = template.Library()

@register.simple_tag
def getFirstYear():
    return CabSalida.getMinYear()

@register.simple_tag
def getCurrentYear():
    return datetime.now().year

