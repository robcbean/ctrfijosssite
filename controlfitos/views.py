from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from controlfitos.models import Agricultor, Cliente, Cultivo, Variedad, TipoTratamiento, Producto

#class Producto(models.Model):
#    nombre = models.CharField(max_length=100)
#    nombreComercial = models.CharField(max_length=100)
#    noregistro = models.CharField(max_length=100)
#    precio = models.FloatField()
#    plazoSeguridad = models.IntegerField()
#    tipoTratamiento = models.ForeignKey(TipoTratamiento,on_delete=models.CASCADE)

class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre','nombreComercial','noregistro','precio','plazoSeguridad','tipoTratamiento']

class ProductoList(ListView):
    model = Producto
    fields = ['nombre','nombreComercial','noregistro','precio','plazoSeguridad','tipoTratamiento']

class TipoTratamientoCreateView(CreateView):
    model = TipoTratamiento
    fields = ['nombre']
    success_url = '/controlfitos/tipotratamiento/list'

class TipoTratamientoList(ListView):
    model = TipoTratamiento
    fields = ['nombre']

class CultivoCreateView(CreateView):
    model = Cultivo
    fields = ['nombre']
    success_url = '/controlfitos/cultivo/list'


class CultivoListView(ListView):
    model = Cultivo
    fields = ['nombre']

class VaridadCreateView(CreateView):
    model = Variedad
    fields = ['nombre','cultivo']
    success_url = '/controlfitos/variedad/list'

class VaridadListView(ListView):
    model = Variedad
    fields = ['nombre','cultivo']


class AgricultorCreateView(CreateView):
    model = Agricultor
    fields = ['nombre','cif','domicilio','cliente','campanya']


class AgricultorUpdateView(UpdateView):
    model = Agricultor
    fields = ['nombre','cif','domicilio','cliente','campanya']

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre','domicilio','cif']
    success_url = '/thanks/'

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre','domicilio','cif']
    success_url = '/thanks/'

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
