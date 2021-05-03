from django.db import models

# Create your models here.


class Cliente(models.Model):
    id = models.AutoField("ID",primary_key=True,blank=False,null=False)
    nombre = models.CharField("Nombre",max_length=60, blank=False, null=False)
    apellidos = models.CharField("Apellidos",max_length=100, blank=True, null=False)
    direccion = models.CharField("Direccion",max_length=100, blank=True, null=True)
    telefono = models.CharField("Telefono cliente",max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Aparato(models.Model):
    TIPO = (
        ('generico', 'Generico'),
        ('comercial', 'Comercial'),
    )
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(choices=TIPO, max_length=30)
    nombre = models.CharField(max_length=200, unique=True)
    fecha_expiracion = models.DateField()
    fecha_produccion = models.DateField()
    descripcion = models.TextField(max_length=400)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre

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


#---------------------------------------------------
#Ventas
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

