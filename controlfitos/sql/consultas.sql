
-- Consulta de kilos por año

SELECT
    YEAR(T0.fecha)
    SUM(T1.cantidad)
	FROM Fitos.CabSalida T0
	JOIN Fitos.Salida T1 ON T1.cabSalidaObjId = T0.serialNum
    JOIN Fitos.Variedad T2 ON T2.serialNum = T1.variedadObjId
    GROUP BY YEAR(T0.fecha)


-- Consulta de kilos por Cultivo

SELECT
	YEAR(T3.fecha)
    ,T0.nombre as "Cultivo"
    ,SUM(T2.cantidad)
    FROM Fitos.Cultivo T0
    JOIN Fitos.Variedad T1 ON T1.cultivoObjId = T0.serialNum
    JOIN Fitos.Salida T2 ON T2.variedadObjId = T1.serialNum
	JOIN Fitos.CabSalida T3 ON T3.serialNum = T2.cabSalidaObjId
    GROUP BY
    	YEAR(T3.fecha)
        ,T0.nombre
