from django.db import models

from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=250)
    cif = models.CharField(max_length=10)

class ConceptoGasto(models.Model):
    comentario = models.CharField(max_length=100)

class Cultivo(models.Model):
    nombre = models.CharField(max_length=100)

class Cultivo(models.Model):
    nombre = models.CharField(max_length=100)

class Variedad(models.Model):
    nombre = models.CharField(max_length=100)
    finalizada = models.IntegerField()

class ConceptoGasto(models.Model):
    comentrio = models.CharField(max_length=100)


class TipoTratamiento(models.Model):
    nombre = models.CharField(max_length=100)


class Gasto(models.Model):
    fecha = models.DateField()
    cultivo = models.ForeignKey(Cultivo,on_delete=models.CASCADE)
    variedad = models.ForeignKey(Variedad,on_delete=models.CASCADE)
    concepto = models.ForeignKey(ConceptoGasto,on_delete=models.CASCADE)


class Agricultor(models.Model):
    nombre = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=250)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    campanya = models.CharField(max_length=100)


class CabSalida(models.Model):
    fecha = models.DateField()

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    nombreComercial = models.CharField(max_length=100)
    noregistro = models.CharField(max_length=100)
    precio = models.FloatField()
    plazoSeguridad = models.IntegerField()
    tipoTratamiento = models.ForeignKey(TipoTratamiento,on_delete=models.CASCADE)

class Salida(models.Model):
    cantidad = models.FloatField()
    precio = models.FloatField()
    albaran = models.CharField(max_length=100)
    factura = models.CharField(max_length=100)
    cabSalida = models.ForeignKey(CabSalida,on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)


#class TipoTratamientoProducto(models.Model):

#class TipoTratamientoTratamiento

class Tratamiento(models.Model):
    fecha = models.DateField()
    precio = models.FloatField()




