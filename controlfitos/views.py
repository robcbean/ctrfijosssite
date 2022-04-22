from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from controlfitos.models import Agricultor, Cliente, Cultivo


class CultivoCreateView(CreateView):
    model = Cultivo
    fields = ['nombre']

class CultivoListView(ListView):
    model = Cultivo
    fields = ['nombre']

class AgricultorCreateView(CreateView):
    model = Agricultor
    fields = ['nombre','domicilio','cliente','campanya']

class AgricultorUpdateView(UpdateView):
    models = Agricultor
    fields = ['nombre','domicilio','campanya']

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
