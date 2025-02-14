
#  CREAR CATEGORIA # 

este enpoint nos permite crear una categoria nueva, donde se rebicen datos que correpnden a los detalles de la categiria que se agregara. 

## REQUERIEMINTOS

    - El cliente, debe de estar autenticado con un token valido
    - La solicitud debe contener los campos validos 

## OBSERVACIONES O CORREIOCNES

    - Se tiene que asegurar que los campos necesarios esten en la solicitud 
    - El campo "nombre" de la categoria debe ser unico
    - el token de autenticacion, no tiene un timepo limite 
    - el campo id,  debe ser nulo, ya que el sistema lo genera automáticamente.
    - el campo fecha_creacion,  se autogenera al momento de la creación.
    - el valor de categoria, debe ser un ID válido de una categoría que ya exista. 

## URL

    - Para categorias 

http://127.0.0.1:8000/api/categorias/ 

http://127.0.0.1:8000/api/categorias/?Authorization=Bearer

    - Para productos

http://127.0.0.1:8000/api/productos/


## METODO HTTP

    - POST

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
|                      |                       |  

Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM5NTM4NjkyLCJpYXQiOjE3Mzk1MzgzOTIsImp0aSI6IjFiMjFlM2ZhNzA5NzQ5OTI4MDgwMjBlNzllNTM4NTQ1IiwidXNlcl9pZCI6M30.


## PARÁMETROS 

| NOMBRE DEL PARAMETRO | VALOR                 | DESCRIPCIÓN                              |
| -------------------- | --------------------- | -----------                              |
|   nombre             | string                | el nombre de la categoria que se agrega  |
| -------------------- | --------------------- | -----------                              |
|   id                 | null                  | El ID del producto
|                      |                       |   (se generará automáticamente)          |
| -------------------- | --------------------- | -----------------------------------------|
|   nombre             |       "Puma negros"   |                     nombre de l producto |
| -------------------- | --------------------- | -------------------- ------------------- |
|      marca                       "PUMA"                      marca del prodcuto         |
| -------------------- | --------------------- | -------------------- ------------------- |
|         precio       |      "1800.00"        |   precio del prodcuto                    |
| -------------------- | --------------------- | -------------------- ------------------- |
|         stock        |      7                |   cantidad en stock                      |
| -------------------- | --------------------- | -------------------- ------------------- |
|        descripcion   |"Tenis negros muy      |  Descripción breve del producto         |
|                      |        versátiles"    | 
| -------------------- | --------------------- | -------------------- ------------------- |
|     fecha_creacion      |    null            | Fecha de creación del producto
|                                              |   (será autogenerada)                    |
| -------------------- | --------------------- | -------------------- ------------------- |
|    categoria         |         3             | ID de la categoría a la que pertenece 
|                      |                       |                el producto               |
| -------------------- | --------------------- | -------------------- ------------------- |




## BODY

| NOMBRE DEL PARAMETRO | VALOR                 | DESCRIPCIÓN                              |
| -------------------- | --------------------- | -----------                              |
|   nombre             | string                | el nombre de la categoria que se agrega  |
| -------------------- | --------------------  | --------------------
|   id                 | number                | El ID del producto
|                      |                       |   (se generará automáticamente)          |
| -------------------- | --------------------- | -----------------------------------------|
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
|     fecha_creacion   | null / string (date)  |      Fecha de creación del producto      |
|                                              |   (será autogenerada)                    |
| -------------------- | --------------------- | -------------------- ------------------- |
|    categoria         |         number             | ID de la categoría a la que pertenece 
|                      |                       |                el producto               |
| -------------------- | --------------------- | -------------------- ------------------- |



## RESPUESTA

    - categorias 

{
  "nombre": "Casuales"
}

    - producto

{
    "id": null,
    "nombre": "Puma negros",
    "marca": "PUMA",
    "precio": "1800.00",
    "stock": 7,
    "descripcion": "Tenis negros muy veratiles",
    "fecha_creacion": null,
    "categoria": 3
  }



## EJEMPLO DE REPUESTA

    - categorias 

{
  "id": 3,
  "nombre": "Casuales"
}

    - producto

{
  "id": 3,
  "nombre": "Puma negros",
  "marca": "PUMA",
  "precio": "1800.00",
  "stock": 7,
  "descripcion": "Tenis negros muy veratiles",
  "fecha_creacion": "2025-02-14T13:07:49.297947Z",
  "categoria": 3
}
