from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(Inicio.as_view(),login_url='login'), name='index'),

    path('crear_cliente/', login_required(CrearCliente.as_view(), login_url='login'),name='crear_cliente'),
    path('listar_cliente/', login_required(ListarCliente.as_view(), login_url='login'), name='listar_cliente'),
    path('editar_cliente/<str:pk>/', login_required(ActualizarCliente.as_view(), login_url='login'), name='editar_cliente'),
    path('eliminar_cliente/<int:pk>/', login_required(eliminar_cliente, login_url='login'), name='eliminar_cliente'),

    path('listar_aparato/', login_required(ListarAparato.as_view(), login_url='login'), name='listar_aparato'),
    path('crear_aparato/', login_required(CrearAparato.as_view(), login_url='login'), name='crear_aparato'),
    path('editar_aparato/<int:pk>/', login_required(ActualizarAparato.as_view(), login_url='login'), name='editar_aparato'),
    path('eliminar_aparato/<int:pk>/', login_required(eliminar_aparato, login_url='login'), name='eliminar_aparato'),

    path('crear_compra/', login_required(CrearCompra.as_view(), login_url='login'),name='crear_compra'),
    path('listar_compra/', login_required(ListarCompra.as_view(), login_url='login'), name='listar_compra'),
    path('eliminar_compra/<int:pk>/', login_required(eliminar_compra, login_url='login'), name='eliminar_compra'),

    path('crear_venta/', login_required(CrearVenta, login_url='login'), name='crear_venta'),
    path('get_clientes/', login_required(get_clientes, login_url='login'), name='get_clientes'),
    path('agregar/<int:pk>/', login_required(agregar_producto, login_url='login'), name='agregar'),
    path('eliminar/<int:pk>/', login_required(eliminar_producto, login_url='login'), name='eliminar'),
    path('restar/<int:pk>/', login_required(restar_producto, login_url='login'), name='restar'),
    path('limpiar/<int:pk>/', login_required(limpiar_carro, login_url='login'), name='limpiar'),
    path('visualizar/', login_required(visualizar_producto, login_url='login'), name='visualizar'),
]
