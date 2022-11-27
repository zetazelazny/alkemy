--Listar los nombres de los proveedores cuya ciudad contenga la cadena de texto �Ramos�.

SELECT Nombre
  FROM Proveedor
 WHERE UPPER(Ciudad) LIKE '%RAMOS%';

--Listar los c�digos de los materiales que provea el proveedor 4 y no los provea el proveedor 5. Se debe resolver de 3 formas.

SELECT Prov_A.CodMat
  FROM Provisto_Por AS Prov_A
 WHERE Prov_A.CodProv = 4
   AND NOT EXISTS (SELECT 1
                     FROM Provisto_Por AS Prov_B
                    WHERE Prov_A.CodMat = Prov_B.CodMat
					  AND Prov_B.CodProv = 5)

SELECT Prov_A.CodMat
  FROM Provisto_Por AS Prov_A
 WHERE Prov_A.CodProv = 4
   AND Prov_A.CodMat NOT IN (SELECT Prov_B.CodMat
                               FROM Provisto_Por AS Prov_B
                              WHERE Prov_B.CodProv = 5)

SELECT Prov_A.CodMat
  FROM Provisto_Por AS Prov_A
 WHERE Prov_A.CodProv = 4
EXCEPT
SELECT Prov_B.CodMat
  FROM Provisto_Por AS Prov_B
 WHERE Prov_B.CodProv = 5

--Listar los materiales, c�digo y descripci�n, provistos por proveedores de la ciudad de Ramos Mej�a.

SELECT Material.CodMat
     , Material.Descripcion
  FROM Provisto_Por
 INNER JOIN Proveedor ON Provisto_Por.CodProv = Proveedor.CodProv
 INNER JOIN Material ON Provisto_Por.CodMat = Material.CodMat
 WHERE UPPER(Proveedor.Ciudad) = 'RAMOS MEJ�A'

--Listar los proveedores y materiales que provee. La lista resultante debe incluir a aquellos proveedores que no proveen
--ning�n material.

SELECT Proveedor.Nombre
     , Material.Descripcion
  FROM Proveedor
 LEFT JOIN Provisto_Por ON Proveedor.CodProv = Provisto_Por.CodProv
 LEFT JOIN Material ON Provisto_Por.CodMat = Material.CodMat

--Listar los art�culos que cuesten m�s de $30 o que est�n compuestos por el material 2.

SELECT *
  FROM Articulo
 WHERE Precio > 30
    OR EXISTS (SELECT 1
	             FROM Compuesto_Por
				WHERE Compuesto_Por.CodArt = Articulo.CodArt
				  AND CodMat = 2)

--Listar los art�culos de Mayor precio.

SELECT *
  FROM Articulo Art_A
 WHERE Art_A.Precio = (SELECT MAX(Art_B.Precio)
                         FROM Articulo Art_B)

--Listar los proveedores que proveen m�s de 3 materiales

SELECT Proveedor.Nombre
  FROM Proveedor
 INNER JOIN Provisto_Por ON Proveedor.CodProv = Provisto_Por.CodProv
GROUP BY Proveedor.Nombre
HAVING COUNT(1) > 3

--Crear una vista para el caso de los proveedores que proveen m�s de 4 materiales. Mostrar la forma de invocar esa vista.

CREATE VIEW Proveedores_4Mats_V AS
SELECT Proveedor.CodProv
     , Proveedor.Nombre
  FROM Proveedor
 INNER JOIN Provisto_Por ON Proveedor.CodProv = Provisto_Por.CodProv
GROUP BY Proveedor.CodProv
       , Proveedor.Nombre
HAVING COUNT(1) > 3

SELECT *
  FROM Proveedores_4Mats_V
