from controlfitos.models import CabSalida
from datetime import datetime
from django.template.base import TemplateSyntaxError

from django import template
register = template.Library()

@register.tag(name='get_years')
def get_years(parser, token):
    class ArrayCreator(template.Node):
        def __init__(self, var_name):
            self.var_name = var_name  # output variable

        def render(self, context):
            anyos = []
            for i in range(CabSalida.getMinYear(),datetime.now().year):
                anyos.append(i)
            context[self.var_name] = anyos
            print(anyos)
            return ''

    args = token.contents.split()  # "create_array", "as", VAR_NAME

    if len(args) != 3 or args[1] != 'as':
        raise TemplateSyntaxError("'create_array' requires 'as variable' (got %r)" % args)

    return ArrayCreator(args[2])

