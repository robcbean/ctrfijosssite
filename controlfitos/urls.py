from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('agricultor/add',views.AgricultorCreateView.as_view(),name='agricultor-add'),
    path('agricultor/<int:pk>/',views.AgricultorUpdateView.as_view(),name='agricultor-update'),

    path('cliente/add',views.ClienteCreateView.as_view(),name='cliente-add'),
    path('cliente/<int:pk>/',views.ClienteUpdateView.as_view(),name='cliente-update'),

    path('cultivo/list', views.CultivoListView.as_view(), name='cultivos-list'),
    path('cultivo/add', views.CultivoCreateView.as_view(), name='cultivos-add'),


    path('variedad/list', views.VaridadListView.as_view(), name='variedad-list'),
    path('variedad/add', views.VaridadCreateView.as_view(), name='varieadd-add'),

    path('tipotratamiento/list', views.TipoTratamientoList.as_view(), name='tipotratamiento-list'),
    path('tipotratamiento/add', views.TipoTratamientoCreateView.as_view(), name='tipotratamiento-add'),

    path('producto/list', views.ProductoList.as_view(), name='producto-list'),
    path('producto/add', views.ProductoCreateView.as_view(), name='producto-add'),

    path('reports/', views.reports, name='reports'),

    path('report/<str:report_id>', views.report, name='report'),






]