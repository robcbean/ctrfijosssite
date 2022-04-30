from controlfitos.models import CabSalida
from datetime import datetime
from django.template.base import TemplateSyntaxError

from django import template
register = template.Library()

@register.tag(name='create_array')
def create_array(parser, token):
    class ArrayCreator(template.Node):
        def __init__(self, var_name):
            self.var_name = var_name  # output variable

        def render(self, context):
            context[self.var_name] = [1, 2, 3, 4]
            #range(CabSalida.getMinYear(),datetime.now().year)
            return ''

    args = token.contents.split()  # "create_array", "as", VAR_NAME

    if len(args) != 3 or args[1] != 'as':
        raise TemplateSyntaxError("'create_array' requires 'as variable' (got %r)" % args)

    return ArrayCreator(args[2])

