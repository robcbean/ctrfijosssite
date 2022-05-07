import datetime
import django
from django.db import models
from django.db import connection


class Cliente(models.Model):
    nombre = models.CharField(max_length=100,default='')
    domicilio = models.CharField(max_length=250,default='')
    cif = models.CharField(max_length=10,default='')
    def __str__(self):
        return self.nombre


class ConceptoGasto(models.Model):
    comentario = models.CharField(max_length=150,default=' ')

class Cultivo(models.Model):
    nombre = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.nombre


class Variedad(models.Model):
    nombre = models.CharField(max_length=100,default='')
    finalizada = models.IntegerField(default=0)
    cultivo = models.ForeignKey(Cultivo,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre


class TipoTratamiento(models.Model):
    nombre = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.nombre


class Agricultor(models.Model):
    nombre = models.CharField(max_length=100,default='')
    campanya = models.CharField(max_length=100,default='')
    domicilio = models.CharField(max_length=250,default='')
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    cif = models.CharField(max_length=10,default='')

    def __str__(self):
        return self.nombre

    @staticmethod
    def getAgricultor():
        ret = Agricultor.objects.all()[0]
        return ret

    @staticmethod
    def getKilos(start_year=0, end_year=0, cultivo_id=0, variedad_id=0):
        query = 'SELECT' \
                '    YEAR(T0.fecha) as "year" ' \
                '    ,SUM(T1.cantidad) as kilos' \
                '	 FROM   controlfitos_cabsalida T0 ' \
                '	 JOIN controlfitos_salida T1 ON T1.cabSalida_id = T0.id' \
                '    JOIN  controlfitos_variedad T2 ON T2.id = T1.variedad_id' \
                '    JOIN  controlfitos_cultivo T3 ON T3.id = T2.cultivo_id' \
                '    WHERE 1=1 ' \

        if start_year != 0:
            query = query + f' AND YEAR(T0.fecha)>={start_year}'

        if end_year != 0:
            query = query + f' AND YEAR(T0.fecha)<={end_year}'

        if cultivo_id != 0:
            query = query + f' AND T3.id = {cultivo_id}'

        if variedad_id != 0:
            query = query + f' AND T2.id = {variedad_id}'

        query = query +  '    GROUP BY YEAR(T0.fecha)'
        years = []
        kilos = []
        cursor = connection.cursor()

        #print(f'Query:\n{query}')
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            years.append(record[0])
            kilos.append(record[1])


        return years,kilos

class CabSalida(models.Model):
    fecha = models.DateField(default=django.utils.timezone.now)
    @staticmethod
    def getMinYear():
        cursor = connection.cursor()
        query = 'SELECT IFNULL(MIN(YEAR(fecha)),0) FROM controlfitos_cabsalida'
        cursor.execute(query)
        result = cursor.fetchall()
        ret = result[0][0]
        return  ret



class Producto(models.Model):
    nombre = models.CharField(max_length=100,default='')
    nombreComercial = models.CharField(max_length=100,default='')
    noregistro = models.CharField(max_length=100,default='')
    plazoSeguridad = models.IntegerField(default=0)
    tipoTratamiento = models.ForeignKey(TipoTratamiento,on_delete=models.CASCADE)
    noDisponible = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Salida(models.Model):
    cantidad = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    fecha = models.DateField(default=django.utils.timezone.now)
    albaran = models.CharField(max_length=100,default='')
    factura = models.CharField(max_length=100,default='')
    cabSalida = models.ForeignKey(CabSalida, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    variedad = models.ForeignKey(Variedad, on_delete=models.CASCADE)

class Tratamiento(models.Model):
    fecha = models.DateField(default=django.utils.timezone.now)
    precio = models.FloatField(default=0)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    def __str__(self):
        ret = f'{str(self.fecha)} {str(self.precio)} {str(self.producto)}'
        return ret

class VariedadesTratamiento(models.Model):
    tratamiento = models.ForeignKey(Tratamiento,on_delete=models.CASCADE)
    variedad = models.ForeignKey(Variedad,on_delete=models.CASCADE)

    @staticmethod
    def delVariedadTramiento(_variedad_tratamiento_id: int, _tratamiento_id: int):
        varidadtratamiento = VariedadesTratamiento.objects.get(pk=_variedad_tratamiento_id)
        varidadtratamiento.delete()
        results = VariedadesTratamiento.objects.filter(tratamiento__id=_tratamiento_id)
        if results.count() == 0:
            tratamiento = Tratamiento.objects.get(pk=_tratamiento_id)
            tratamiento.delete()

    @staticmethod
    def addVariedadTratamiento(_date: datetime.date, _producto_id: int, _variedad_id : int):
        ret = True
        if _producto_id == None or _variedad_id == None or _date == "":
            ret = False

        results = Tratamiento.objects.filter(fecha=_date,producto_id=_producto_id)
        if results.count() == 0:
            tratamiento = Tratamiento()
            tratamiento.fecha = _date
            tratamiento.producto = Producto.objects.get(pk=_producto_id)
            tratamiento.save()
        else:
            tratamiento = results[0]

        results = VariedadesTratamiento.objects.filter(tratamiento_id=tratamiento.id,variedad_id=_variedad_id)
        if results.count() == 0:
            varidadestratamiento = VariedadesTratamiento()
            varidadestratamiento.variedad = Variedad.objects.get(pk=_variedad_id)
            varidadestratamiento.tratamiento = tratamiento
            varidadestratamiento.save()






