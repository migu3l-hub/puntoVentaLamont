from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from electronica.models import Item, Cliente, Compra


class FormularioLogin(
    AuthenticationForm):  # ESTA SOBREESCRITURA PARA PONER ESTILOS SE PODRIA HACER CON djamgo_widget_tw
    def __init__(self, *args, **kwargs):  # es el metodo que ejecuta toda clase de python lo redifinimos
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'input100'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['username'].widget.attrs['type'] = 'text'
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'input100'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password'].label = 'Contraseña'


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs[
                'autocomplete'] = 'off'  # Es mas facil con django widget_tweaks ejemplo en crear cliente
        print(self.fields.keys())
        self.fields['nombre'].widget.attrs[
            'placeholder'] = 'Ingrese el nombre del cliente'  # Ejemplo cambiar algo a un solo campo

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'direccion',
                  'telefono']  # Es el orden en que regresa los keys del diccionario de arriba
        labels = {
            'nombre': 'Nombre del cliente',
            'apellidos': 'Apellidos del cliente',
            'direccion': 'Direccion del cliente',
            'telefono': 'Telefono del cliente',
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'id': 'usr'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese los apellidos del cliente',
                    'id': 'pwd'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese la direccion del cliente',
                    'id': 'nombres'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el telefono del cliente',
                    'id': 'apellidos'
                }
            ),
        }


class AparatoForm(forms.ModelForm):
    class Meta:
        model = Item
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
            'precio_venta': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Precio de Compra'}
            ),
            'stock': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Existentes en el almacen'}
            ),
            'nombre': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nombre del aparato'}
            ),
            'tipo': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'fecha_expiracion': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'fecha_produccion': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
        }


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ('marca', 'cantidad', 'item')
        label = {
            'marca': 'Marca',
            'cantidad': 'Cantidad comprada',
            'item': 'Producto',
        }
        widgets = {
            'marca': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'cantidad': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'item': forms.Select(
                attrs={'class': 'form-control'}
            ),
        }
