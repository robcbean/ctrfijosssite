import sys

from controlfitos.models import Producto,Variedad,Agricultor,Tratamiento,VariedadesTratamiento
from django.template.base import TemplateSyntaxError
from django import template

register = template.Library()
@register.tag(name='get_variedades_tratamientos')
def get_variedades_tratamientos(parser,token):
    class ArrayCreator(template.Node):

        def __init__(self, var_name):
            self.var_name = var_name  # output variable
        def render(self, context):
            start_date,end_date = Agricultor.getAgricultor().getCampanyDates()
            variedad_tratamientos = []
            for variedad_tratamiento in VariedadesTratamiento.objects.filter(tratamiento__fecha__gte=start_date).order_by("tratamiento__fecha"):
                variedad_tratamientos.append(variedad_tratamiento)
            context[self.var_name] = variedad_tratamientos
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


@register.tag(name='get_productos')
def get_productos(parser,token):

    class ArrayCreator(template.Node):

        def __init__(self, var_name):
            self.var_name = var_name  # output variable

        def render(self, context):
            productos = []
            producto = Producto()
            producto.nombre = "______"
            productos.append(producto)
            for producto in Producto.objects.filter(noDisponible=False).order_by('nombre'):
                productos.append(producto)
            context[self.var_name] = productos
            return ''

    args = token.contents.split()  # "create_array", "as", VAR_NAME

    if len(args) != 3 or args[1] != 'as':
        raise TemplateSyntaxError("'create_array' requires 'as variable' (got %r)" % args)

    return ArrayCreator(args[2])
