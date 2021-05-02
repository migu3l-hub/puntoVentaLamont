from django.contrib.auth.forms import AuthenticationForm
from django import forms
from electronica import api
from electronica.models import Aparato, Cliente


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):  # es el metodo que ejecuta toda clase de python lo redifinimos
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'input100'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['username'].widget.attrs['type'] = 'text'
        self.fields['password'].widget.attrs['class'] = 'input100'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'direccion', 'telefono']
        labels = {
            'nombre': 'Nombre del cliente',
            'apellidos': 'Apellidos del cliente',
            'direccion': 'Direccion del cliente',
            'telefono': 'Telefono del cliente',
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del cliente',
                    'id': 'usr'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese los apellidos del cliente',
                    'id': 'pwd'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la direccion del cliente',
                    'id': 'nombres'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el telefono del cliente',
                    'id': 'apellidos'
                }
            ),
        }


class AparatoForm(forms.ModelForm):
    class Meta:
        model = Aparato
        fields = ('tipo', 'nombre', 'fecha_expiracion', 'fecha_produccion', 'descripcion', 'precio_venta', 'stock')
        label = {
            'tipo': 'Tipo de aparato',
            'nombre': 'Nombre de aparato',
            'fecha_expiracion': 'Fecha de fecha_expiracion del aparato',
            'fecha_produccion': 'Fecha de produccion del aparato',
            'descripcion': 'Descripcion del aparato',
            'precio_venta': 'Precio de venta',
            'stock': 'Stock en el almacen',
        }
        widgets = {
            'descripcion': forms.Textarea(
                attrs={'class': 'form-control', 'rows': '6', 'placeholder': 'Pequeña Descripcion'}
            ),
            'precio_Compra': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Precio de Compra'}
            ),
            'precio_venta': forms.NumberInput(
                attrs={'class': 'form-control', 'id': 'valor3', 'placeholder': 'Precio de Venta'}
            ),
            'presentacion': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'tipo': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'fecha_expiracion': forms.DateInput(
                attrs={'class': 'form-control', 'id': 'Date', 'data-date-format': 'dd/mm/yyyy'}),
            'fecha_produccion': forms.DateInput(
                attrs={'class': 'form-control', 'id': 'Date1', 'data-date-format': 'dd/mm/yyyy'}),
        }