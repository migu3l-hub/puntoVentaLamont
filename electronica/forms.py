from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from electronica import api
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
    # MML verificacion de Contraseña
    pwd2 = forms.CharField(label='Contraseña de confirmación', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Ingrese de nuevo la contraseña',
            'id': 'pwd2',
            'required': 'required',
        }
    ))

    class Meta:
        model = User
        fields = ('email','first_name','last_name','password')
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electronico',
            'first_name': 'Nombre real',
            'last_name': 'Apellidos',
            'password':'Contraseña',
        }

        widgets = {
            # 'username': forms.TextInput(
            #     attrs={
            #         'class': 'form-control py-4',
            #         'placeholder': 'Nombre de usuario'
            #     }
            # ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control py-4',
                    'placeholder': 'Correo electronico'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control py-4',
                    'placeholder': 'Nombre de usuario'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control py-4',
                    'placeholder': 'Apellidos'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control py-4',
                    'placeholder': 'Contraseña'
                }
            ),
        }

    def clean_pwd2(self):  # MML Hacemos la verificacion de si la contraeña coincide
        pwd1 = self.cleaned_data['password']
        pwd2 = self.cleaned_data['pwd2']
        if pwd1 != pwd2:
            raise forms.ValidationError('Las contraseñas no coinciden')  # Este es el error que esta en forms.error
        return pwd2

    def save(self, commit=True):
        user = super().save(commit=False)  # MML se redefine la forma en que se guarda la contraseña
        print("Estoy en el save")
        pwd_hash = api.hashear_contrasena(self.cleaned_data['password'])
        user.password = pwd_hash
        if commit:
            user.save()
        return user


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
