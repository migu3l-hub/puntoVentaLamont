from django.contrib.auth import authenticate, logout as do_logout
from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from . import decorators
from .forms import FormularioLogin, AparatoForm, ClienteForm, CompraForm, ClienteVenta, RegistroUsuario
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, TemplateView
from .models import Item, Cliente, Compra
from django.contrib.auth.models import User
from .api import Carro


# Create your views here.


# @axes_dispatch
# @decorators.no_esta_logueado
# def login(request):
#     if request.method == "POST":  # GIG POST significa que el usuario envio datos que debemos procesar
#         nomusuario = request.POST.get("username")
#         pwdenviada = request.POST.get("password")
#         user = authenticate(request=request, username=nomusuario, password=pwdenviada)
#         if user is not None:
#             try:
#                 do_login(request, user)
#                 return redirect('global:index')
#             except Exception:
#                 return render(request, 'login.html', {"form": FormularioLogin, "errores": "Error al iniciar sesión"})
#         else:
#             return render(request, 'login.html',
#                           {"form": FormularioLogin, "errores": "Usuario y/o contraseña inválidos."})
#     elif request.method == "GET":
#         return render(request, "login.html", {"form": FormularioLogin})


class Login(LoginView):  # Por defecto usa todos los backends
    template_name = "login.html"  # Automaticamente si esta bien lo redirecciona a donde diga el settings
    authentication_form = FormularioLogin  # Los errores son tratados en el propio html con form.errors y salen con swee
    redirect_authenticated_user = True


class Registro(CreateView):
    model = User
    form_class = RegistroUsuario
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_invalid(self, form):
        errores = form.errors
        context = {"errores":errores, "form": RegistroUsuario}
        return render(self.request, "register.html", context)


def logout(request):
    do_logout(request)
    return redirect("login")


class Inicio(TemplateView):  # las vistas basadas en clases tienen los metodos get_context_data get post y dispatch
    template_name = 'global/index.html'


class ListarCliente(ListView):
    model = Cliente
    template_name = 'global/listar_cliente.html'
    context_object_name = 'clientes'
    queryset = Cliente.objects.all()


class ActualizarCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'global/crear_cliente.html'
    success_url = reverse_lazy('global:listar_cliente')


class CrearCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'global/crear_cliente.html'
    success_url = reverse_lazy('global:listar_cliente')


class EliminarCliente(DeleteView):
    model = Cliente
    success_url = reverse_lazy('global:listar_cliente')


class CrearAparato(CreateView):
    model = Item
    form_class = AparatoForm
    template_name = 'global/crear_aparato.html'
    success_url = reverse_lazy('global:listar_aparato')


class ListarAparato(ListView):  # MML esta incompleto
    model = Item
    template_name = 'global/listar_aparato.html'
    context_object_name = 'aparatos'
    queryset = Item.objects.all()

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):  # ESTA USANDO POST AUNQUE NO SE REONOCE COMO FUNCION DE LA CLASE
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                print("Entre al if")
                data = []
                for i in Item.objects.all():
                    data.append(
                        i.toJSON())  # El array lleva un conjunto de diccionarios pero datatable lo toma como objetos cada dic
            else:
                data['error'] = "Ha ocurrido un error"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,
                            safe=False)  # Se debe poner el safe en false cuando se envia mas de un diccionario para que se serialize


class ActualizarAparato(UpdateView):
    model = Item
    form_class = AparatoForm
    template_name = 'global/crear_aparato.html'
    success_url = reverse_lazy('global:listar_aparato')


class EliminarAparato(DeleteView):
    model = Item
    success_url = reverse_lazy('global:listar_aparato')


class CrearCompra(CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'global/crear_compra.html'
    success_url = reverse_lazy('global:listar_compra')

    def post(self, request, *args, **kwargs):
        compra_form = CompraForm(request.POST)
        if compra_form.is_valid():
            compra_form.save()
        pk = request.POST["item"]
        cantidad = request.POST["cantidad"]

        item = Item.objects.get(id=pk)
        newstock = item.stock + int(cantidad)
        item.stock = newstock
        item.save()
        return redirect('global:listar_compra')



class ListarCompra(ListView):
    model = Compra
    template_name = 'global/listar_compra.html'
    context_object_name = 'compras'
    queryset = Compra.objects.all()


def CrearVenta(request):
    carro = Carro(request)
    if request.method == 'POST':
        if request.method["itemid"]:
            item = request.POST["itemid"]
            print(item)
    action = request.GET.get('action')
    print(action)
    if action is not None:
        items = Item.objects.filter(nombre__icontains=action)
        print(items)
        data = []
        for i in items:
            data.append(i.toJSON())
        return JsonResponse(data, safe=False)
    # form2 = ClienteVenta()
    context = carro.get_cliente()
    total = carro.get_total()
    context["total"] = total
    print(context)
    return render(request, 'global/crear_venta.html', context)


@csrf_exempt
def get_clientes(request):
    carro = Carro(request)
    global options, response
    if request.method == 'GET':
        print("hola")
        name = request.GET.get('name')
        clientes = Cliente.objects.none()
        options = '<option value="" selected="selected">---------</option>'
        if name:
            clientes = Cliente.objects.filter(nombre__icontains=name)
        for cliente in clientes:
            completo = cliente.nombre + " " + cliente.apellidos
            options += '<option value="%s">%s</option>' % (
                cliente.pk,
                completo
            )
        response = {'clientes': options}
    if request.method == 'POST':
        ide = request.POST.get('selected')
        print("aqui")
        cliente = Cliente.objects.get(id=ide)
        carro.agregar_cliente(cliente=cliente)
        nombre = cliente.nombre
        apellidos = cliente.apellidos
        telefono = cliente.telefono
        response = {'nombre': nombre, 'apellidos': apellidos, 'telefono': telefono}
    return JsonResponse(response)


def eliminar_compra(request, pk=0):
    compra = Compra.objects.get(id=pk)
    compra.delete()
    return redirect('global:listar_compra')


def eliminar_aparato(request, pk=0):
    aparato = Item.objects.get(id=pk)
    aparato.delete()
    return redirect('global:listar_aparato')


def eliminar_cliente(request, pk=0):
    cliente = Cliente.objects.get(id=pk)
    cliente.delete()
    return redirect('global:listar_cliente')


def agregar_producto(request, pk=0):
    cantidad = 1

    carro = Carro(request)

    if request.GET.get("cantidad"):
        cantidad = request.GET.get("cantidad")

    producto = Item.objects.get(id=pk)

    total = carro.agregar(producto=producto, cantidad=cantidad)

    return redirect("global:crear_venta")


def eliminar_producto(request, pk=0):
    carro = Carro(request)

    producto = Item.objects.get(id=pk)

    carro.eliminar(producto=producto)

    return redirect("global:crear_venta")


def restar_producto(request, producto_id):
    carro = Carro(request)

    producto = Item.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)

    return redirect("global:crear_venta")


def limpiar_carro(request):
    carro = Carro(request)

    carro.limpiar_carro()

    carro.eliminar_cliente()

    return redirect("global:crear_venta")


# modificando
def visualizar_producto(request, pk=0):
    producto = Item.objects.get(id=pk)
    return render(request, 'global/visualizar_producto.html',
                  {'id_producto': producto.id, 'tipo_producto': producto.tipo,
                   'nombre_producto': producto.nombre, 'fecha_expiracion': producto.fecha_expiracion,
                   'fecha_produccion': producto.fecha_produccion, 'descripcion_producto': producto.descripcion,
                   'precio_compra': producto.precio_compra, 'precio_venta': producto.precio_venta,
                   'stock_prodcuto': producto.stock})
