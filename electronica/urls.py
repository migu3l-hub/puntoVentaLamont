from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(Inicio.as_view(),login_url='login'), name='index'),

    path('crear_cliente/', login_required(CrearCliente.as_view(),login_url='login'),name='crear_cliente'),
    path('listar_cliente/', login_required(ListarCliente.as_view(), login_url='login'), name='listar_cliente'),
    path('editar_cliente/<str:pk>/', login_required(ActualizarCliente.as_view(), login_url='login'), name='editar_cliente'),
    path('eliminar_cliente/<str:pk>/', login_required(EliminarCliente.as_view(), login_url='login'), name='eliminar_cliente'),

    path('listar_aparato/', login_required(ListarAparato.as_view(),login_url='login'), name='listar_aparato'),
    path('crear_aparato/', login_required(CrearAparato.as_view(), login_url='login'), name='crear_aparato'),
    path('editar_aparato/<int:pk>/', login_required(ActualizarAparato.as_view(), login_url='login'), name='editar_aparato'),
    path('eliminar_aparato/<int:pk>/', login_required(EliminarAparato.as_view(), login_url='login'), name='eliminar_aparato'),

    path('crear_compra/', login_required(CrearCompra.as_view(),login_url='login'),name='crear_compra'),
    path('listar_compra/', login_required(ListarCompra.as_view(), login_url='login'), name='listar_compra'),
    path('eliminar_compra/<int:pk>/', login_required(eliminar_compra, login_url='login'), name='eliminar_compra'),
]
