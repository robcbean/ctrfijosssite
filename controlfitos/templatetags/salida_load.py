from controlfitos.models import Cliente,Variedad
from django.template.base import TemplateSyntaxError
from django import template


register = template.Library()


@register.tag(name='get_variedades')
def get_variedades(parser,token):

    class ArrayCreator(template.Node):

        def __init__(self, var_name):
            self.var_name = var_name  # output variable
        def render(self, context):

            variedades = []
            variedad = Variedad()
            variedad.nombre = "_____"
            variedades.append(variedad)
            for variedad in Variedad.objects.all().order_by('nombre'):
                variedades.append(variedad)
            context[self.var_name] = variedades
            return ''

    args = token.contents.split()  # "create_array", "as", VAR_NAME

    if len(args) != 3 or args[1] != 'as':
        raise TemplateSyntaxError("'create_array' requires 'as variable' (got %r)" % args)

    return ArrayCreator(args[2])


@register.tag(name='get_clientes')
def get_productos(parser,token):

    class ArrayCreator(template.Node):

        def __init__(self, var_name):
            self.var_name = var_name  # output variable

        def render(self, context):
            clientes = []
            cliente = Cliente()
            cliente.nombre = "______"
            clientes.append(cliente)
            for cliente in Cliente.objects.all().order_by('nombre'):
                clientes.append(cliente)
            context[self.var_name] = clientes
            return ''

    args = token.contents.split()  # "create_array", "as", VAR_NAME

    if len(args) != 3 or args[1] != 'as':
        raise TemplateSyntaxError("'create_array' requires 'as variable' (got %r)" % args)

    return ArrayCreator(args[2])
