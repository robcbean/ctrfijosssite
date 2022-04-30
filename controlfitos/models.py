import datetime
import sys

import django
from django.db import models
from django.db import connection


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

    @staticmethod
    def getKilos(start_year=0, end_year=0, cultivo_id=0, variedad_id=0):
        query = 'SELECT' \
                '    YEAR(T0.fecha) as "year" ' \
                '    ,SUM(T1.cantidad) as kilos' \
                '	 FROM   controlfitos_cabsalida T0 ' \
                '	 JOIN controlfitos_salida T1 ON T1.cabSalida_id = T0.id' \
                '    JOIN  controlfitos_variedad T2 ON T2.id = T1.variedad_id' \
                '    WHERE 1=1 ' \

        if start_year != 0:
            query = query + f' AND YEAR(T0.fecha)>={start_year}'

        if end_year != 0:
            query = query + f' AND YEAR(T0.fecha)<={end_year}'

        query = query +  '    GROUP BY YEAR(T0.fecha)'
        years = []
        kilos = []
        cursor = connection.cursor()

        print(f'Query:\n{query}')

        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            years.append(record[0])
            kilos.append(record[1])


        return years,kilos

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
    fecha = models.DateField(default=datetime.date.today())
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





