use SQL_DML

--Listar los nombres de los proveedores cuya ciudad contenga la cadena de texto “Ramos”.
SELECT *
  FROM Proveedor
 WHERE UPPER(Ciudad) LIKE '%RAMOS%'

-- Listar los códigos de los materiales que provea el proveedor 4 y no los provea el proveedor 5. Se debe resolver de 3 formas.

--NOT IN
SELECT CodMat
  FROM Provisto_Por
 WHERE CodProv = 4
   AND CodProv NOT IN (SELECT CodMat
                         FROM Provisto_Por
						WHERE CodProv = 5)

--NOT EXISTS
SELECT PP_A.CodMat
  FROM Provisto_Por AS PP_A
 WHERE PP_A.CodProv = 4
   AND NOT EXISTS (SELECT 1
                     FROM Provisto_Por AS PP_B
					WHERE PP_B.CodMat = PP_A.CodMat
					  AND PP_B.CodProv = 5)

--EXCEPT
SELECT CodMat
  FROM Provisto_Por
 WHERE CodProv = 4
EXCEPT
SELECT CodMat
  FROM Provisto_Por
 WHERE CodProv = 5

--Listar los materiales, código y descripción, provistos por proveedores de la ciudad de Ramos Mejía.
SELECT Material.CodMat
     , Material.Descripcion
  FROM Material
 INNER JOIN Provisto_Por ON Material.CodMat = Provisto_Por.CodMat
 INNER JOIN Proveedor ON Provisto_Por.CodProv = Proveedor.CodProv
 WHERE UPPER(Proveedor.Ciudad) LIKE '%RAMOS%'

--Listar los proveedores y materiales que provee. La lista resultante debe incluir a aquellos proveedores que no proveen ningún material.
SELECT Proveedor.Nombre
     , Provisto_Por.CodMat
  FROM Proveedor
  LEFT JOIN Provisto_Por ON Proveedor.CodProv = Provisto_Por.CodProv

--Listar los artículos que cuesten más de $30 o que estén compuestos por el material 2.
SELECT *
  FROM Articulo
 WHERE Precio > 30
    OR EXISTS (SELECT 1
	             FROM Compuesto_Por
				WHERE Compuesto_Por.CodArt = Articulo.CodArt
				  AND Compuesto_Por.CodMat = 2)

--Listar los artículos de Mayor precio.
SELECT *
  FROM Articulo
 WHERE Precio = (SELECT MAX(Precio)
                   FROM Articulo)

--Listar los proveedores que proveen más de 3 materiales
SELECT Proveedor.Nombre
     , COUNT(1) AS Cant_Arts_Provistos
  FROM Provisto_Por
 INNER JOIN Proveedor ON Provisto_Por.CodProv = Proveedor.CodProv
 GROUP BY Proveedor.Nombre
HAVING COUNT(1) > 3

--Crear una vista para el caso de los proveedores que proveen más de 4 materiales. Mostrar la forma de invocar esa vista.

CREATE VIEW [dbo].[Proveedores_4Mats_V] AS
SELECT Proveedor.CodProv
     , Proveedor.Nombre
  FROM Proveedor
 INNER JOIN Provisto_Por ON Proveedor.CodProv = Provisto_Por.CodProv
GROUP BY Proveedor.CodProv
       , Proveedor.Nombre
HAVING COUNT(1) > 3

SELECT * 
  FROM Proveedores_4Mats_V