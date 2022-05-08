import datetime
from django.template import loader
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from controlfitos.models import Agricultor, Cliente, Cultivo, TipoTratamiento, Producto,  VariedadesTratamiento, Variedad, Salida
from controlfitos.reporting.reports import  OutputReports


outputReport = OutputReports()


class EditGrid:
    AddIcon = "add-48.png"
    DelIcon = "delete-48.png"
    EditIcon = "edit-48.png"
    SaveIcon = "save-48.png"


class Reports:
    KilosPorAnyo = "kilosporanyo"
    KilosPorVaridad = "kilosporvariedad"

class ProductoCreateView(CreateView):
    model = Producto
    fields = '__all__'
    success_url = '/controlfitos/producto/list'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


class ProductoUpdateView(UpdateView):
    model = Producto
    fields = '__all__'
    success_url = '/controlfitos/producto/list'


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


class ProductoList(ListView):
    model = Producto
    fields = '__all__'
    ordering = ['name']

    def get_initial(self):
        return {'check_todos': 'off'}


    def get_context_data(self,  **kwargs):
        todos = self.request.GET.get('todos')
        context = super(ProductoList, self).get_context_data(**kwargs)
        qs = kwargs.pop('object_list', self.object_list)
        if todos == None or todos == "off":
            context['check_todos'] = ''
        else:
            context['check_todos'] = 'checked=true'
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)



    def get_queryset(self, **kwargs):
        todos = self.request.GET.get('todos')
        print(f'Todos:{todos}\n')
        if todos == None or todos == "":
            productos = Producto.objects.filter(noDisponible=False)
        else:
            productos = Producto.objects.all()
        return productos


class TipoTratamientoUpdateView(UpdateView):
    model = TipoTratamiento
    fields = ['nombre']
    success_url = '/controlfitos/tipotratamiento/list'
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


class CultivoUpdateView(UpdateView):
    model = Cultivo
    fields = ['nombre']
    success_url = '/controlfitos/cultivo/list'
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
    #fields = ['nombre', 'cultivo',]
    fields = '__all__'
    success_url = '/controlfitos/variedad/list'
    def __init__(self,*args,**kwargs):

        super(VaridadCreateView, self).__init__(*args,**kwargs)
        #self.fields['cultivo'].label_from_instance = self.label_from_instance

    @staticmethod
    def label_from_instance(obj):
        print(obj.nombre)
        return obj.nombre

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


class VaridadUpdateView(UpdateView):
    model = Variedad
    fields = '__all__'
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
    success_url = "/controlfitos/"
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
    context = {
               'KilosPorAnyo' : Reports.KilosPorAnyo,
               'KilosPorVaridad': Reports.KilosPorVaridad,
    }
    return HttpResponse(template.render(context,request))


def tratamientos(request,variedad_tratamiento_id=0,tratamiento_id=0):

    if variedad_tratamiento_id !=0 and tratamiento_id != 0:
        VariedadesTratamiento.delVariedadTramiento(_variedad_tratamiento_id=variedad_tratamiento_id,_tratamiento_id=tratamiento_id)
        return redirect('/controlfitos/tratamientos/')
    else:
        if request.method == 'POST':
            VariedadesTratamiento.addVariedadTratamiento(request.POST.get("fecha"),request.POST.get("producto"),request.POST.get("variedad"))
            return redirect('/controlfitos/tratamientos/')
        template = loader.get_template("controlfitos/tratamientos_template.html")
        campanya = Agricultor.getAgricultor().campanya
        if campanya == '':
            raise Exception(f'Debe especificar la campaña en el agricultor')

        campanya = int(campanya)
        start_date = datetime.date(campanya,1,1)
        end_date = datetime.date(campanya,12,31)
        variedadestramiento = VariedadesTratamiento.objects.filter(tratamiento__fecha__gte=start_date).filter(tratamiento__fecha__lte=end_date).order_by('-tratamiento__fecha')

        context = {
            'variedadestramiento' : variedadestramiento,
            'editicon': EditGrid.EditIcon,
            'addicon': EditGrid.AddIcon,
            'delicon': EditGrid.DelIcon,
            'saveicon': EditGrid.SaveIcon,
        }
        return HttpResponse(template.render(context, request))

def salidas(request,salida_id=0):
    template = loader.get_template("controlfitos/salidas_template.html")
    if salida_id != 0:
        Salida.delSalida(salida_id)
        return redirect('/controlfitos/salidas/')
    else:
        if request.method == 'POST':
            Salida.addSalida(request.POST.get('cliente'),request.POST.get('fecha'),request.POST.get('albaran'),request.POST.get('variedad'),request.POST.get('cantidad'))
            return redirect('/controlfitos/salidas/')
        campanya = Agricultor.getAgricultor().campanya
        client_id = Agricultor.getAgricultor().cliente.id
        print(client_id)
        if campanya == '':
            raise Exception(f'Debe especificar la campaña en el agricultor')

        campanya = int(campanya)
        start_date = datetime.date(campanya, 1, 1)
        end_date = datetime.date(campanya, 12, 31)
        salidas = Salida.objects.filter(cabSalida__fecha__gte=start_date).filter(
            cabSalida__fecha__lte=end_date).order_by('-cabSalida__fecha')

        context = {
            'salidas' : salidas,
            'cliente_id': client_id,
            'editicon': EditGrid.EditIcon,
            'addicon': EditGrid.AddIcon,
            'delicon': EditGrid.DelIcon,
            'saveicon': EditGrid.SaveIcon,
        }
        return HttpResponse(template.render(context, request))


def report(request,report_id,start_year=0,end_year=0,cultivo=0,variedad=0):
    file_image = ""
    base_name = ""
    template = loader.get_template("controlfitos/report_template.html")

    if request.method == 'POST':
        start_year = request.POST.get('start_year')
        end_year = request.POST.get('end_year')
        if start_year != '':
            start_year = int(start_year)
        if end_year != '':
            end_year = int(end_year)

    if report_id == Reports.KilosPorAnyo:
        #print(f'exportando fichero de salida')
        anyos, kilos = Agricultor.getKilos(start_year=start_year, end_year=end_year, cultivo_id=cultivo, variedad_id=variedad)
        base_name = f'{report_id}.jpg'
        file_name = f'static/{base_name}'
        out_file_image = f'controlfitos/{file_name}'
        outputReport.reportYearTotalEvolution(anyos,kilos,out_file_image)
    context = {
        'report_id'  : report_id,
        'report_img' : base_name,
        'start_year' : start_year,
        'end_year' : end_year,
        'cultivo_id' : cultivo,
        'variedad_id' : variedad,
    }
    #print(f'Report_id:{report_id}\t{file_image}')
    return HttpResponse(template.render(context,request))


def index(request):
    context = {}
    template = loader.get_template("controlfitos/base_template.html")
    return HttpResponse(template.render(context,request))
