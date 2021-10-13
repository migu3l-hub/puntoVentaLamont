from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from electronica.models import Item, Cliente, Compra, Venta


class FormularioLogin(
    AuthenticationForm):  # ESTA SOBREESCRITURA PARA PONER ESTILOS SE PODRIA HACER CON djamgo_widget_tw
    def __init__(self, *args, **kwargs):  # es el metodo que ejecuta toda clase de python lo redifinimos
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control py-4'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control py-4'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password'].label = 'Contraseña'

class RegistroUsuario(UserCreationForm):
    def __init__(self, *args, **kwargs):  # AQUI SE MODIFICAN LOS CAMPOS POR QUE SON DE LA CLASE USERCREATIONFORM
        super(RegistroUsuario, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control py-4'
        self.fields['username'].widget.attrs['placeholder'] = 'Ingresar nombre de usuario'
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['first_name'].widget.attrs['class'] = 'form-control py-4'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Ingresar nombre real'
        self.fields['first_name'].label = 'Nombre de persona'
        self.fields['last_name'].widget.attrs['class'] = 'form-control py-4'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellidos'
        self.fields['last_name'].label = 'Ingresar apellidos'
        self.fields['email'].widget.attrs['class'] = 'form-control py-4'
        self.fields['email'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['email'].label = 'Nombre de usuario'
        self.fields['password1'].widget.attrs['class'] = 'form-control py-4'
        self.fields['password1'].widget.attrs['placeholder'] = 'Ingresar la contraseña'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].widget.attrs['class'] = 'form-control py-4'
        self.fields['password2'].widget.attrs['placeholder'] = 'Ingresa la misma contraseña'
        self.fields['password2'].label = 'Contraseña de confirmacion'

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1', 'password2')


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'  # Es mas facil con django widget_tweaks
        print(self.fields.keys())
        self.fields['nombre'].widget.attrs[
            'placeholder'] = 'Ingrese el nombre del cliente'  # Ejemplo cambiar algo a un solo campo

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'direccion', 'telefono']  # Es el orden en que regresa los keys del diccionario
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
        fields = ('marca', 'cantidad', 'item', 'precio')
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
            'precio': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
        }


class ClienteVenta(forms.Form):
    clientes = forms.ModelChoiceField(
        label=u'Cliente',
        queryset=Cliente.objects.all()
    )

    def __init__(self, *args, **kwargs):
        super(ClienteVenta, self).__init__(*args, **kwargs)
        self.fields['clientes'].queryset = Cliente.objects.none()
        self.fields['clientes'].widget.attrs['required'] = False


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ('serie', 'despachador')
        label = {
            'marca': 'Marca',
            'cantidad': 'Cantidad comprada',
            'item': 'Producto',
        }
        widgets = {
            'serie': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'despachador': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }
