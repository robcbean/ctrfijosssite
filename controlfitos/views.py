from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView
from controlfitos.models import Agricultor, Cliente

#nombre = models.CharField(max_length=100)
#domicilio = models.CharField(max_length=250)
#cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#campanya = models.CharField(max_length=100)


class AgricultorCreateView(CreateView):
    model = Agricultor
    fields = ['nombre','domicilio','cliente','campanya']
    success_url = '/thanks/'


class AgricultorUpdateView(UpdateView):
    models = Agricultor
    fields = ['nombre','domicilio','cliente','campanya']
    success_url = '/thanks/'


class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre','domicilio','cif']
    success_url = '/thanks/'
    submit_name = 'Añadir'

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre','domicilio','cif']
    success_url = '/thanks/'
    submit_name = 'Actualizar'

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
