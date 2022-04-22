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


]