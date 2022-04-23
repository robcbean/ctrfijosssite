#!/usr/bin/env python3
import pymysql
from reports import OutputReports

consulta = "SELECT \n" \
    "YEAR(T0.fecha)\n" \
    ",SUM(T1.cantidad)\n"  \
	" FROM Fitos.CabSalida T0\n" \
	" JOIN Fitos.Salida T1 ON T1.cabSalidaObjId = T0.serialNum \n" \
    " JOIN Fitos.Variedad T2 ON T2.serialNum = T1.variedadObjId \n" \
    " GROUP BY YEAR(T0.fecha) "

con = pymysql.Connection(user='roberto',password='iluvatar',database='Fitos',host='192.168.0.251')
cur = con.cursor()

outReport = OutputReports()

cur.execute(consulta)
result = cur.fetchall()
x = []
y = []
for record in result:
    x.append(record[0])
    y.append(record[1])


con.close()

outReport.reportYearTotalEvolution(x,y,"/Users/rbean/temp/test.png")

