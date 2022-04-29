
from django.template import loader
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from controlfitos.models import Agricultor, Cliente, Cultivo, Variedad, TipoTratamiento, Producto
from controlfitos.reporting.reports import  OutputReports


outputReport = OutputReports()


class Reports:
    KilosPorAnyo = "kilosporanyo"
    KilosPorVaridad = "kilosporvariedad"

class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre','nombreComercial','noregistro','precio','plazoSeguridad','tipoTratamiento']
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


class ProductoList(ListView):
    model = Producto
    fields = ['nombre','nombreComercial','noregistro','precio','plazoSeguridad','tipoTratamiento']
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


class TipoTratamientoCreateView(CreateView):
    model = TipoTratamiento
    fields = ['nombre']
    success_url = '/controlfitos/tipotratamiento/list'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


class TipoTratamientoList(ListView):
    model = TipoTratamiento
    fields = ['nombre']
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)

class CultivoCreateView(CreateView):
    model = Cultivo
    fields = ['nombre']
    success_url = '/controlfitos/cultivo/list'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


class CultivoListView(ListView):
    model = Cultivo
    fields = ['nombre']
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


class VaridadCreateView(CreateView):
    model = Variedad
    fields = ['nombre','cultivo']
    success_url = '/controlfitos/variedad/list'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


class VaridadListView(ListView):
    model = Variedad
    fields = ['nombre','cultivo']
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)



class AgricultorCreateView(CreateView):
    model = Agricultor
    fields = ['nombre','cif','domicilio','cliente','campanya']
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)



class AgricultorUpdateView(UpdateView):
    model = Agricultor
    fields = ['nombre','cif','domicilio','cliente','campanya']
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre','domicilio','cif']
    success_url = '/thanks/'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre','domicilio','cif']
    success_url = '/thanks/'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)

def reports(request):
    template = loader.get_template("controlfitos/reports_template.html")
    context = {}
    return HttpResponse(template.render(context,request))


def report(request,report_id):
    file_image = ""
    template = loader.get_template("controlfitos/report_template.html")
    if report_id == Reports.KilosPorAnyo:
        print(f'exportando fichero de salida')
        agricultor = Agricultor()
        anyos, kilos = agricultor.getKilosPorAnyo()
        file_name = f'static/{report_id}.jpg'
        out_file_image = f'controlfitos/{file_name}'
        outputReport.reportYearTotalEvolution(anyos,kilos,out_file_image)
    context = {
        'report_id'  : report_id,
        'report_img' : file_image,
    }
    print(f'Report_id:{report_id}\t{file_image}')
    return HttpResponse(template.render(context,request))


def index(request):
    template = loader.get_template("controlfitos/base_template.html")
    context = {}
    return HttpResponse(template.render(context,request))
