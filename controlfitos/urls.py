from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('tratamientos/',views.tratamientos),
    path('salidas/',views.salidas),

    path('agricultor/add',views.AgricultorCreateView.as_view(),name='agricultor-add'),
    path('agricultor/<int:pk>/',views.AgricultorUpdateView.as_view(),name='agricultor-update'),

    path('cliente/add',views.ClienteCreateView.as_view(),name='cliente-add'),
    path('cliente/<int:pk>/',views.ClienteUpdateView.as_view(),name='cliente-update'),

    path('cultivo/list', views.CultivoListView.as_view(), name='cultivos-list'),
    path('cultivo/add', views.CultivoCreateView.as_view(), name='cultivos-add'),
    path('cultivo/<int:pk>', views.CultivoUpdateView.as_view(), name='cultivos-update'),


    path('variedad/list', views.VaridadListView.as_view(), name='variedad-list'),
    path('variedad/add', views.VaridadCreateView.as_view(), name='varieadd-add'),
    path('variedad/<int:pk>', views.VaridadUpdateView.as_view(), name='varieadd-add'),

    path('tipotratamiento/list', views.TipoTratamientoList.as_view(), name='tipotratamiento-list'),
    path('tipotratamiento/add', views.TipoTratamientoCreateView.as_view(), name='tipotratamiento-add'),

    path('producto/list', views.ProductoList.as_view(), name='producto-list'),
    path('producto/add', views.ProductoCreateView.as_view(), name='producto-add'),
    path('producto/<int:pk>', views.ProductoUpdateView.as_view(), name='producto-update'),


    path('reports/', views.reports, name='reports'),
    path('reports/<str:report_id>/', views.report),
    path('reports/<str:report_id>/<int:start_year>/',views.report),
    path('reports/<str:report_id>/<int:start_year>/<int:end_year>',views.report),
    path('reports/<str:report_id>/<int:start_year>/<int:end_year>/<int:cultivo>',views.report),
    path('reports/<str:report_id>/<int:start_year>/<int:end_year>/<int:cultivo>/<int:variedad>',views.report),

]