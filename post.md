
#  CREAR CATEGORIA # 

este enpoint nos permite crear una categoria nueva, donde se rebicen datos que correpnden a los detalles de la categiria que se agregara. 

## REQUERIEMINTOS

    - El cliente, debe de estar autenticado con un token valido
    - La solicitud debe contener los campos validos 

## OBSERVACIONES O CORREIOCNES

    - Se tiene que asegurar que los campos necesarios esten en la solicitud 
    - El campo "nombre" de la categoria debe ser unico

## URL

http://127.0.0.1:8000/api/categorias/ 

http://127.0.0.1:8000/api/categorias/?Authorization=Bearer 

## METODO PHP 

    - POST

## HEADERS 

| HEADER               | VALOR                 | DESCRIPCIÓN                            |
| -------------------- | --------------------- | -----------                            |
|
|   Accept             | */*                   | acepta cualquier tipo de respuesta 
|    
| -------------------- | --------------------  | --------------------               
|                      |                       |                                        |
|   User-Agent         | Thunder client        | el cliente que se usa para realizar la  
|                      |                       |  solicitud              
| -------------------- | --------------------  | --------------------
|                      |                       |                                        |
| Authorization        | Bearer    (token)     | el token de autenticacion del cliente  |
|                      |                       |  

Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM5NTM4NjkyLCJpYXQiOjE3Mzk1MzgzOTIsImp0aSI6IjFiMjFlM2ZhNzA5NzQ5OTI4MDgwMjBlNzllNTM4NTQ1IiwidXNlcl9pZCI6M30.


## PARÁMETROS 

| NOMBRE DEL PARAMETRO | VALOR                 | DESCRIPCIÓN                              |
| -------------------- | --------------------- | -----------                              |
|   nombre             | string                | el nombre de la categoria que se agrega  |
| -------------------- | --------------------  | --------------------

## BODY

| NOMBRE DEL PARAMETRO | VALOR                 | DESCRIPCIÓN                              |
| -------------------- | --------------------- | -----------                              |
|   nombre             | string                | el nombre de la categoria que se agrega  |
| -------------------- | --------------------  | --------------------


## RESPUESTA

{
  "nombre": "Casuales"
}

## EJEMPLO DE REPUESTA

{
  "id": 3,
  "nombre": "Casuales"
}

