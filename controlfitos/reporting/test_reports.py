#!/usr/bin/env python3
import pymysql
from reports import OutputReports






con = pymysql.Connection(user='roberto',password='iluvatar',database='FitosNew',host='192.168.0.251')
cur = con.cursor()
query = 'SELECT IFNULL(MIN(YEAR(fecha)),0) FROM controlfitos_cabsalida'
cur.execute(query)
result = cur.fetchall()
print(result[0])

#print(qry)





