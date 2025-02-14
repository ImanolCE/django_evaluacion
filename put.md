
## ACTUALIZAR UN PRODUCTO

este endpoint nos pemrite actualizar la informaiocn de un producto que ya existe.


## REQUERIEMINTOS

    - contar con un token de autenticación válido.

    - el id del producto, debe existir en la base de datos.

    - enviar la solicitud con el formato adecuado para que se realize la peticion de la petición.


## OBSERVACIONES O CORREIOCNES

    - asegurarse que los datos que se vayan a cambiar sean del tipo de dato corecto.
    - la categoria de de ser un id valido, que exista.

## URL

http://127.0.0.1:8000/api/productos/3

## METODO HTTP

PUT

## HEADERS 

| HEADER               | VALOR                 | DESCRIPCIÓN                            |
| -------------------- | --------------------- | -----------                            |
|   Accept             | */*                   | acepta cualquier tipo de respuesta     |    
| -------------------- | --------------------  | --------------------                   |
|                      |                       |                                        |
|   User-Agent         | Thunder client        | el cliente que se usa para realizar la |
|                      |                       |  solicitud                             |
| -------------------- | --------------------  | --------------------                   |
|                      |                       |                                        |
| Authorization        | Bearer    (token)     | el token de autenticacion del cliente  |
|               

Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM5NTU0MzAwLCJpYXQiOjE3Mzk1NTQwMDAsImp0aSI6Ijk0MTY4N2VjOGEzMDQ2NDdiMmIyZDE4OTMwMDJkMjk5IiwidXNlcl9pZCI6M30.SO5gVjJ_7adzVeV4EmKxWo5ZzvNRFVtTy4j-9hs6K7k       |                       |  

## PARÁMETROS 

| NOMBRE DEL PARAMETRO | VALOR                 | DESCRIPCIÓN                              |
| -------------------- | --------------------- | -----------                              |
|   id                 | int/number            | El ID del producto                       |
|                      |                       |   a actualizar                           |
| -------------------- | --------------------- | -----------------------------------------|


## BODY

## BODY

| CLAVE                | VALOR                 | DESCRIPCIÓN                              |
| -------------------- | --------------------- | -----------                              |
|   nombre             |       string          |            nombre de l producto           |
| -------------------- | --------------------- | -------------------- ------------------- |
|      marca                       string      |               marca del prodcuto         |
| -------------------- | --------------------- | -------------------- ------------------- |
|         precio       |      string (decimal) |         precio del prodcuto              |      
| -------------------- | --------------------- | -------------------- ------------------- |
|         stock        |      integer          |        cantidad en stock                 |
| -------------------- | --------------------- | -------------------- ------------------- |
|        descripcion   |       string          | Descripción breve del producto           |
| -------------------- | --------------------- | -------------------- ------------------- |
|    categoria         |         number        | ID de la categoría a la que pertenece 
|                      |                       |                el producto               |
| -------------------- | --------------------- | -------------------- ------------------- |



## RESPUESTA

 {
    "nombre": "Puma negros actualizados",
    "marca": "PUMA",
    "precio": 2900.00,
    "stock": 2,
    "descripcion": "Tenis negros actualizados con mejor diseño",
    "categoria": 3
 }


## EJEMPLO DE REPUESTA

{
  "id": 3,
  "nombre": "Puma negros actualizados",
  "marca": "PUMA",
  "precio": "2900.00",
  "stock": 2,
  "descripcion": "Tenis negros actualizados con mejor diseño",
  "fecha_creacion": "2025-02-14T13:07:49.297947Z",
  "categoria": 3
}



