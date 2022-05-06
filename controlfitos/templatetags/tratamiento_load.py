from controlfitos.models import Producto
from django.template.base import TemplateSyntaxError
from django import template


register = template.Library()

@register.tag(name='get_productos')
def get_productos(parser,token):

    class ArrayCreator(template.Node):

        def __init__(self, var_name):
            self.var_name = var_name  # output variable

        def render(self, context):
            productos = []
            for producto in Producto.objects.filter(noDisponible=False):
                productos.append(producto)
            context[self.var_name] = productos
            return ''

    args = token.contents.split()  # "create_array", "as", VAR_NAME

    if len(args) != 3 or args[1] != 'as':
        raise TemplateSyntaxError("'create_array' requires 'as variable' (got %r)" % args)

    return ArrayCreator(args[2])
