from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(inicio,login_url='login'), name='index'),
    path('login/', login_global, name='login_global'),

    path('crear_admin/', login_required(CrearCliente.as_view(),login_url='login'),name='crear_admin'),
    path('listar_admin/', login_required(ListarCliente.as_view(), login_url='login'), name='listar_admin'),
    path('editar_admin/<str:pk>/', login_required(ActualizarCliente.as_view(), login_url='login'), name='editar_admin'),
    path('eliminar_admin/<str:pk>/', login_required(EliminarCliente.as_view(), login_url='login'), name='eliminar_admin'),

    path('listar_server/', login_required(ListarAparato.as_view(),login_url='login'), name='listar_server'),
    path('crear_server/', login_required(CrearAparato.as_view(), login_url='login'), name='crear_server'),
    path('editar_server/<int:pk>/', login_required(ActualizarAparato.as_view(), login_url='login'), name='editar_server'),
    path('eliminar_server/<int:pk>/', login_required(EliminarAparato.as_view(), login_url='login'), name='eliminar_server')
]
