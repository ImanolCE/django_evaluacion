
## OBTENER PRODUCTOS 

este endpoint nos prmite tener los detalles de los productos que estan registrados


## REQUERIEMINTOS

    - el cliente debe de estar autenticado con un token valido 
    - se puede aplicar fitros para un producto en especfico
    - el token de autenticacion, no tiene un timepo limite 


## OBSERVACIONES O CORRECCIONES

    - si no se especifica ningun parametro, se devolveran los productos que esten disponibles 
    - 

## URL

http://127.0.0.1:8000/api/productos/

http://127.0.0.1:8000/api/productos/1


## METODO HTTP

GET

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

Baerear eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM5NTU0MjExLCJpYXQiOjE3Mzk1NTM5MTEsImp0aSI6ImY4MjBmMThmZTM2ZTRiYmJiNWJmNTU1ODA2NDQ1Nzk2IiwidXNlcl9pZCI6M30.ERrC8Z_jPK6GL3WWbU7hHWfHPhUN-HdXEG1XKEDYd-E

## PARÁMETROS 

| NOMBRE DEL PARAMETRO | VALOR                 | DESCRIPCIÓN                              |
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



## RESPUESTA

    - aqui se hace la peticion, con la URl de http://127.0.0.1:8000/api/productos/  , aparecen todos 
    - y con la URL mas un id, http://127.0.0.1:8000/api/productos/1

## EJEMPLO DE REPUESTA

   - sin especificar un filtro

[
  {
    "id": 1,
    "nombre": "Puma Court",
    "marca": "PUMA",
    "precio": "1200.00",
    "stock": 7,
    "descripcion": "Tenis tipo retro muy veratiles",
    "fecha_creacion": "2025-02-13T21:50:16.453554Z",
    "categoria": 1
  },
  {
    "id": 2,
    "nombre": "Grand Court",
    "marca": "addidas",
    "precio": "1500.00",
    "stock": 5,
    "descripcion": "Tenis blancos con franjas negras, para dias deportivos",
    "fecha_creacion": "2025-02-14T12:33:32.257778Z",
    "categoria": 1
  },
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
]


    - especificando tan siquiera un id 

{
  "id": 1,
  "nombre": "Puma Court",
  "marca": "PUMA",
  "precio": "1200.00",
  "stock": 7,
  "descripcion": "Tenis tipo retro muy veratiles",
  "fecha_creacion": "2025-02-13T21:50:16.453554Z",
  "categoria": 1
}

