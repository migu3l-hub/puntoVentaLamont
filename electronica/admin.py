from django.contrib import admin

# Register your models here.
from electronica.models import Item, Marca, Compra, Venta

admin.site.register(Item),
admin.site.register(Marca),
admin.site.register(Compra),
admin.site.register(Venta),
