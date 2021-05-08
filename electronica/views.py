from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from axes.decorators import axes_dispatch
from . import decorators
from .forms import FormularioLogin, AparatoForm, ClienteForm
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import Aparato, Cliente


# Create your views here.


@axes_dispatch
@decorators.no_esta_logueado
def login(request):
    if request.method == "POST":  # GIG POST significa que el usuario envio datos que debemos procesar
        nomusuario = request.POST.get("username")
        pwdenviada = request.POST.get("password")
        user = authenticate(request=request, username=nomusuario, password=pwdenviada)
        if user is not None:
            try:
                do_login(request, user)
                return redirect('global:index')
            except Exception:
                return render(request, 'login.html', {"form": FormularioLogin, "errores": "Error al iniciar sesión"})
        else:
            return render(request, 'login.html',
                          {"form": FormularioLogin, "errores": "Usuario y/o contraseña inválidos."})
    elif request.method == "GET":
        return render(request, "login.html", {"form": FormularioLogin})


def logout(request):
    do_logout(request)
    return redirect("login")


@axes_dispatch
@decorators.no_esta_logueado
def login_global(request):
    if request.method == 'POST':
        nomuser = request.POST.get("username")
        conuser = request.POST.get("password")
        user = authenticate(request, username=nomuser, password=conuser)
        if user is not None:
            if user.is_superuser:
                try:
                    do_login(request, user)
                    return redirect('global:index')
                except Exception:
                    return render(request, 'global/login_global.html',
                                  {"form": FormularioLogin, "errores": "Error al iniciar sesión"})
            else:
                return render(request, 'login.html',
                              {"form": FormularioLogin, "errores": "Usuario por favor inicia sesion aquí."})
        else:
            return render(request, 'global/login_global.html',
                          {"form": FormularioLogin, "errores": "Usuario y/o contraseña inválidos."})
    elif request.method == "GET":
        return render(request, "global/login_global.html", {"form": FormularioLogin})


@decorators.no_es_admin
def inicio(request):
    if request.method == "GET":
        return render(request, 'global/index.html')


@decorators.class_view_decorator(decorators.no_es_admin)
class ListarCliente(ListView):
    model = Cliente
    template_name = 'global/listar_cliente.html'
    context_object_name = 'clientes'
    queryset = Cliente.objects.all()


@decorators.class_view_decorator(decorators.no_es_admin)
class ActualizarCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'global/crear_cliente.html'
    success_url = reverse_lazy('global:listar_cliente')


@decorators.class_view_decorator(decorators.no_es_admin)
class CrearCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'global/crear_cliente.html'
    success_url = reverse_lazy('global:listar_cliente')


@decorators.class_view_decorator(decorators.no_es_admin)
class EliminarCliente(DeleteView):
    model = Cliente
    success_url = reverse_lazy('global:listar_cliente')


@decorators.class_view_decorator(decorators.no_es_admin)
class CrearAparato(CreateView):
    model = Aparato
    form_class = AparatoForm
    template_name = 'global/crear_aparato.html'
    success_url = reverse_lazy('global:listar_aparato')


@decorators.class_view_decorator(decorators.no_es_admin)
class ListarAparato(ListView):  # MML esta incompleto
    model = Aparato
    template_name = 'global/listar_aparato.html'
    context_object_name = 'aparatos'
    queryset = Aparato.objects.all()


@decorators.class_view_decorator(decorators.no_es_admin)
class ActualizarAparato(UpdateView):
    model = Aparato
    form_class = AparatoForm
    template_name = 'global/crear_aparato.html'
    success_url = reverse_lazy('global:listar_aparato')


@decorators.class_view_decorator(decorators.no_es_admin)
class EliminarAparato(DeleteView):
    model = Aparato
    success_url = reverse_lazy('global:listar_aparato')
