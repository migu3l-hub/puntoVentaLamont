from django.db import models

# Create your models here.
from django.forms import model_to_dict


class Cliente(models.Model):
    id = models.AutoField("ID", primary_key=True, blank=False, null=False)
    nombre = models.CharField("Nombre", max_length=60, blank=False, null=False)
    apellidos = models.CharField("Apellidos", max_length=100, blank=True, null=False)
    direccion = models.CharField("Direccion", max_length=100, blank=True, null=True)
    telefono = models.CharField("Telefono cliente", max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)  # Se toma el modelo del que se esta hablando y se convierte en un diccionario
        return item  # Devuelve todos los atributos como un diccionario asi funciona como JSON


class Item(models.Model):
    TIPO = (
        ('generico', 'Generico'),
        ('comercial', 'Comercial'),
    )
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(choices=TIPO, max_length=30)
    nombre = models.CharField(max_length=100, unique=True)
    fecha_expiracion = models.DateField()
    fecha_produccion = models.DateField()
    descripcion = models.TextField(max_length=400)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.PositiveSmallIntegerField(default=0)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, default="", blank=False)

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(null=False, default=0, blank=False)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    precio = models.FloatField(null=False, default=0.00, blank=False)


class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    serie = models.IntegerField(null=True, unique=True)
    despachador = models.CharField(max_length=80, null=False, default="", blank=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False, default="")
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(null=True, default=0, blank=False)
    total = models.IntegerField(null=True, default=0.00, blank=False)
    fecha = models.DateTimeField(auto_now=True)


# class Relacion(models.Model):
#     venta = models.ForeignKey(Venta, on_delete=models.CASCADE, null=True)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
#     cantidad = models.IntegerField(null=True, default=0, blank=False)
#     total = models.IntegerField(null=True, default=0.00, blank=False)
#     cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)

    # def preeciototal(self):
    #     precio_total=self.precio_Compra*self.stock
    #     return precio_total
    #
    # def estadomedicamentos(self):
    #     hoy = datetime.date.today()
    #     dias = (self.fecha_expiracion - hoy).days
    #     return dias
    #
    # def incrementarlote(self, *args, **kwargs):
    #     if self.lote == 0:
    #         self.lote += 1
    #         self.save()
    #     super(Medicamentos, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     if self.precio_venta:
    #      self.igv = round(float(self.precio_venta) * TAX_VALUE, 3)
    #      super(Medicamentos, self).save(*args, **kwargs)
    #     else:
    #      self.igv=0
    #      super(Medicamentos, self).save(*args, **kwargs)

# ---------------------------------------------------
# Ventas
#
# class TimeStampModel(models.Model):
#
#     created = models.DateField(auto_now_add=True)
#     modified = models.DateField(auto_now=True)
#
#     class Meta:
#          abstract = True
#
#
# class Cabecera_Venta(TimeStampModel):
#     ruc = models.CharField(max_length=10, unique=True)
#     cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
#     fecha = models.DateTimeField(auto_now_add=True)
#
#     def __unicode__(self):
#         return self.ruc
#
#
# class todo_item(models.Model):
#     list_id=models.ForeignKey(Cabecera_Venta, on_delete=models.CASCADE)
#     medicamento=models.ForeignKey(Medicamentos, on_delete=models.CASCADE)
#     cantidad=models.IntegerField(max_length=9)
#
#
# def update_stock(sender, instance, **kwargs):
#     instance.medicamento.stock -= instance.cantidad
#     instance.medicamento.save()
#
#
# signals.post_save.connect(update_stock, sender=todo_item, dispatch_uid="update_stock_count")
