from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from axes.decorators import axes_dispatch
from . import decorators
from .forms import FormularioLogin, ServerForm, AdminForm
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import Aparato


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


# Vistas administrador global ##############
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
    model = User
    template_name = 'global/listar_cliente.html'
    context_object_name = 'admins'
    queryset = User.objects.filter(is_superuser=False)


@decorators.class_view_decorator(decorators.no_es_admin)
class ActualizarCliente(UpdateView):
    model = User
    form_class = AdminForm
    template_name = 'global/crear_cliente.html'
    success_url = reverse_lazy('global:listar_admin')


@decorators.class_view_decorator(decorators.no_es_admin)
class CrearCliente(CreateView):
    model = User
    form_class = AdminForm
    template_name = 'global/crear_cliente.html'
    success_url = reverse_lazy('global:listar_admin')


@decorators.class_view_decorator(decorators.no_es_admin)
class EliminarCliente(DeleteView):
    model = User
    success_url = reverse_lazy('global:listar_admin')


@decorators.class_view_decorator(decorators.no_es_admin)
class CrearAparato(CreateView):
    model = Aparato
    form_class = ServerForm
    template_name = 'global/crear_aparato.html'
    success_url = reverse_lazy('global:listar_server')


@decorators.class_view_decorator(decorators.no_es_admin)
class ListarAparato(ListView):  # MML esta incompleto
    model = Aparato
    template_name = 'global/listar_aparato.html'
    context_object_name = 'servers'
    queryset = Aparato.objects.all()


@decorators.class_view_decorator(decorators.no_es_admin)
class ActualizarAparato(UpdateView):
    model = Aparato
    form_class = ServerForm
    template_name = 'global/aparato.html'
    success_url = reverse_lazy('global:listar_server')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servers'] = Aparato.objects.filter(estado=True)
        return context


@decorators.class_view_decorator(decorators.no_es_admin)
class EliminarAparato(DeleteView):
    model = Aparato
    success_url = reverse_lazy('global:listar_server')
