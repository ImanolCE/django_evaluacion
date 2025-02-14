
## DELET DE PRODUCTO

este endpoint nos permite eleminar ya sea un producto o categoria, en este caso un producto. 

## REQUERIEMINTOS

    - se requiere un id válido del producto a eliminar.

    - es necesario contar con un token de autenticación válido

## OBSERVACIONES O CORREIOCNES

    - Se creo otro producto para poder borrarlo, en este caso se creo el producto con el id 6 

## URL

http://127.0.0.1:8000/api/productos/5

## METODO HTTP

DELETE

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

Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM5NTU0MzI5LCJpYXQiOjE3Mzk1NTQwMjksImp0aSI6ImJkNDhlYmZmYjc5ZTQxNmQ4ZDllZjNlZGI4NTg0ODhhIiwidXNlcl9pZCI6M30.gQeSYsGehvlyzTNz0Mpe98op8IrIU36aENJ4hXdwrsU


## PARÁMETROS 

| NOMBRE DEL PARAMETRO | VALOR                 | DESCRIPCIÓN                              |
| -------------------- | --------------------- | -----------                              |
|   id                 | number                   | El ID del producto                    |
|                      |                       |   a eliminar                             |
| -------------------- | --------------------- | -----------------------------------------|



## RESPUESTA

    - productos antes de borrar 

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
    "nombre": "Puma negros actualizados",
    "marca": "PUMA",
    "precio": "2900.00",
    "stock": 2,
    "descripcion": "Tenis negros actualizados con mejor diseño",
    "fecha_creacion": "2025-02-14T13:07:49.297947Z",
    "categoria": 3
  },
  {
    "id": 6,
    "nombre": "Addidas negros niño",
    "marca": "ADDIDAS",
    "precio": "1200.00",
    "stock": 15,
    "descripcion": "Tenis negros muy veratiles para niño",
    "fecha_creacion": "2025-02-14T17:16:13.707651Z",
    "categoria": 1
  }
]



## EJEMPLO DE REPUESTA

    - producto al momento de buscarlo
{
  "detail": "No Producto matches the given query."
}
