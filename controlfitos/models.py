

import django
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100,default='')
    domicilio = models.CharField(max_length=250,default='')
    cif = models.CharField(max_length=10,default='')

class ConceptoGasto(models.Model):
    comentario = models.CharField(max_length=150,default=' ')

class Cultivo(models.Model):
    nombre = models.CharField(max_length=100,default='')

class Variedad(models.Model):
    nombre = models.CharField(max_length=100,default='')
    finalizada = models.IntegerField(default=0)
    cultivo = models.ForeignKey(Cultivo,on_delete=models.CASCADE)


class TipoTratamiento(models.Model):
    nombre = models.CharField(max_length=100,default='')


class Gasto(models.Model):
    fecha = models.DateField(default=django.utils.timezone.now)
    cultivo = models.ForeignKey(Cultivo,on_delete=models.CASCADE)
    variedad = models.ForeignKey(Variedad,on_delete=models.CASCADE)
    concepto = models.ForeignKey(ConceptoGasto,on_delete=models.CASCADE)


class Agricultor(models.Model):
    nombre = models.CharField(max_length=100,default='')
    campanya = models.CharField(max_length=100,default='')
    domicilio = models.CharField(max_length=250,default='')
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    cif = models.CharField(max_length=10,default='')

class CabSalida(models.Model):
    fecha = models.DateField(default=django.utils.timezone.now)

class Producto(models.Model):
    nombre = models.CharField(max_length=100,default='')
    nombreComercial = models.CharField(max_length=100,default='')
    noregistro = models.CharField(max_length=100,default='')
    precio = models.FloatField(default=0)
    plazoSeguridad = models.IntegerField(default=0)
    tipoTratamiento = models.ForeignKey(TipoTratamiento,on_delete=models.CASCADE)

class Salida(models.Model):
    cantidad = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    albaran = models.CharField(max_length=100,default='')
    factura = models.CharField(max_length=100,default='')
    cabSalida = models.ForeignKey(CabSalida, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    variedad = models.ForeignKey(Variedad, on_delete=models.CASCADE)

class Tratamiento(models.Model):
    fecha = django.utils.timezone.now
    precio = models.FloatField(default=0)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)

class VariedadesTratamiento(models.Model):
    tratamiento = models.ForeignKey(Tratamiento,on_delete=models.CASCADE)
    variedad = models.ForeignKey(Variedad,on_delete=models.CASCADE)
    cantidad = models.FloatField(default=0)





