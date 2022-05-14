from controlfitos.models import Cliente,Variedad,Salida,Agricultor
from django.template.base import TemplateSyntaxError
from django import template


register = template.Library()


@register.tag(name='get_salidas')
def get_salidas(parser,token):

    class ArrayCreator(template.Node):

        def __init__(self, var_name):
            self.var_name = var_name  # output variable
        def render(self, context):
            salidas = []
            start_date,end_date = Agricultor.getAgricultor().getCampanyDates()
            for salida in Salida.objects.filter(cabSalida__fecha__gte=start_date).filter(cabSalida__fecha__lte=end_date).order_by('cabSalida__fecha'):
                salidas.append(salida)
            context[self.var_name] = salidas
            return ''

    args = token.contents.split()  # "create_array", "as", VAR_NAME

    if len(args) != 3 or args[1] != 'as':
        raise TemplateSyntaxError("'create_array' requires 'as variable' (got %r)" % args)

    return ArrayCreator(args[2])



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
