# Book Wishlist

Book Wishlist es una aplicación web que consume la API de Google Books donde se podrán consultar libros por titulo, autor y/o editorial, además se podrán consultar las estanterías publicas de un usuario, para poder realizar estas consultas es necesario registrar un usuario e iniciar sesión ya que si el usuario no se autentica no podrá acceder a los endpoints.

## Run

Luego de clonar el repositorio, se utilizara la terminal para instalar librerías, realizar migraciones y ejecutar la aplicación:

Para instalar librerías se utilizara el comando:

```terminal
pip install -r requirements.txt
```
las librerías se instalaran automáticamente y una vez hayan finalizado es necesario realizar migraciones:
```terminal
python manage.py makemigrations
python manage.py migrate
```
Con estos comandos se crearan los campos correspondientes en la base de datos SQLite, por ultimo para ejecutar la aplicación web se requiere el comando:
```terminal
python manage.py runserver
```
## Endpoints
A continuación estos son los endpoints con su respectiva funcionalidad.

## Sing-up
Para realizar el registro se utiliza el endpoint (http://localhost:8000/signup/) por medio del método POST y en el body deberá ir un JSON con el username y password que el usuario desee.

Request

```
{
    "username":"carlost",
    "password":"1ngr3s0"
}
```
Response
```
{
    "id": 1,
    "last_login": null,
    "is_superuser": false,
    "first_name": "",
    "last_name": "",
    "email": "",
    "is_staff": false,
    "is_active": true,
    "date_joined": "2021-11-06T15:04:36.686805-05:00",
    "username": "carlost",
    "groups": [],
    "user_permissions": []
}
```
## Login
Para iniciar sesión se utiliza el endpoint (http://localhost:8000/login/) por medio del método POST y en el body deberá ir un JSON con el username y password correspondiente.

Request

```
{
    "username":"carlost",
    "password":"1ngr3s0"
}
```
Response

Recibirá un token, no es necesario enviar este token en los headers o utilizarlo al momento de hacer algún request ya que automáticamente se almacenará como cookie, la API le retorna el token solo a manera de información.
```
{
    "jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwiZXhwIjoxNjM2MjMzMzkwLCJpYXQiOjE2MzYyMjk3OTB9.ZubK4RNsEl1SQYWw9SuzVarExbe3IkHQVmeXXbO9ZkQ"
}
```

## Logout
Para cerrar sesión se utiliza el endpoint (http://localhost:8000/logout/) por medio del método POST y el body vacío, no es necesario ingresar ninguna información.

Request

```
```
Response
```
{
    "message": "success"
}
```

## Consultar Libros por titulo, autor y editorial

Endpoint (http://localhost:8000/api/search-book/<titulo>/<autor>/<editorial>/<key=ApiKey>).

Metodo GET

Reemplace <titulo>,<autor>,<editorial> por los datos que desea buscar, además reemplace <key=ApiKey> por la apikey correspondiente, el body es vacío.

Request

```
http://localhost:8000/api/search-book/harry/rowling/scholastic/key=AIzaSyAKic6K3QaIGvl7wHLD8E4nfEItz4XElyQ
```

Response
```
{
        "ID": "MCPjwAEACAAJ",
        "Titulo": "Harry Potter and the Goblet of Fire: The Illustrated Edition",
        "Autor": [
            "J. K. Rowling"
        ],
        "Editorial": "Arthur A. Levine Books"
}
```

## Consultar Libros por titulo y autor

Endpoint (http://localhost:8000/api/search-bookTA/<titulo>/<autor>/<key=ApiKey>).

Metodo GET

Reemplace <titulo> y <autor> por los datos que desea buscar, además reemplace <key=ApiKey> por la apikey correspondiente, el body es vacío.

Request

```
http://localhost:8000/api/search-bookTA/harry+potter/rowling/key=AIzaSyAKic6K3QaIGvl7wHLD8E4nfEItz4XElyQ
```

Response
```
{
        "ID": "XLVvAAAACAAJ",
        "Titulo": "Harry Potter Y la Piedra Filosofal",
        "Autor": [
            "J. K. Rowling"
        ]
}
```

## Consultar Libros por titulo y editorial

Endpoint (http://localhost:8000/api/search-bookTP/<titulo>/<editorial>/<key=ApiKey>).

Metodo GET

Reemplace <titulo> y <editorial> por los datos que desea buscar, además reemplace <key=ApiKey> por la apikey correspondiente, el body es vacío.

Request

```
http://localhost:8000/api/search-bookTP/harry+potter/scholastic/key=AIzaSyAKic6K3QaIGvl7wHLD8E4nfEItz4XElyQ
```

Response
```
{
        "ID": "uCKvLmFfc84C",
        "Titulo": "Harry Potter Handbook, Movie Magic",
        "Editorial": "Scholastic Inc."
}
```

## Consultar Libros por autor y editorial

Endpoint (http://localhost:8000/api/search-bookAP/<autor>/<editorial>/<key=ApiKey>).

Metodo GET

Reemplace <autor> y <editorial> por los datos que desea buscar, además reemplace <key=ApiKey> por la apikey correspondiente, el body es vacío.

Request

```
http://localhost:8000/api/search-bookAP/rowling/scholastic/key=AIzaSyAKic6K3QaIGvl7wHLD8E4nfEItz4XElyQ
```

Response
```
{
        "ID": "UwYpEAAAQBAJ",
        "Autor": [
            "J. K. Rowling"
        ],
        "Editorial": "Scholastic Inc."
}
```

## Consultar todas las estanterías publicas de un usuario

Endpoint (http://localhost:8000/api/my-bookshelve-all/<user>/<key=ApiKey>).

Metodo GET

Reemplace <user> con el ID del usuario al que desea consultar la información, además reemplace <key=ApiKey> por la apikey correspondiente, el body es vacío.

Request

```
http://localhost:8000/api/my-bookshelve-all/115859379337770019662/key=AIzaSyAKic6K3QaIGvl7wHLD8E4nfEItz4XElyQ
```

Response
```
{
    "kind": "books#bookshelves",
    "items": [
        {
            "kind": "books#bookshelf",
            "id": 0,
            "title": "Favorites",
            "access": "PUBLIC",
            "updated": "2021-11-06T03:56:37.507Z",
            "created": "2021-11-06T03:56:37.507Z",
            "volumeCount": 5,
            "volumesLastUpdated": "2021-11-06T03:56:37.500Z"
        },
        {
            "kind": "books#bookshelf",
            "id": 3,
            "title": "Reading now",
            "access": "PUBLIC",
            "updated": "2021-11-06T03:56:11.315Z",
            "created": "2021-11-06T03:56:11.315Z",
            "volumeCount": 1,
            "volumesLastUpdated": "2021-11-06T03:56:11.308Z"
        },
        {
            "kind": "books#bookshelf",
            "id": 2,
            "title": "To read",
            "access": "PUBLIC",
            "updated": "2021-11-06T03:57:09.772Z",
            "created": "2021-11-06T03:57:09.772Z",
            "volumeCount": 2,
            "volumesLastUpdated": "2021-11-06T03:57:09.765Z"
        },
        {
            "kind": "books#bookshelf",
            "id": 4,
            "title": "Have read",
            "access": "PUBLIC",
            "updated": "2021-11-06T02:31:03.295Z",
            "created": "2021-11-06T02:31:03.295Z",
            "volumeCount": 1,
            "volumesLastUpdated": "2021-11-06T02:31:03.288Z"
        }
    ]
}
```

## Consultar estanterías especificas publicas de un usuario

Endpoint (http://localhost:8000/api/my-bookshelve-specific/<user>/<bookshelve>/<key=ApiKey>).

Metodo GET

Reemplace <user> con el ID del usuario al que desea consultar la información y <bookshelve> con el numero de la estantería (los números de las estanterías publicas son 0,2,3,4) que desea consultar, además reemplace <key=ApiKey> por la apikey correspondiente, el body es vacío.

Request

```
http://localhost:8000/api/my-bookshelve-specific/115859379337770019662/0/key=AIzaSyAKic6K3QaIGvl7wHLD8E4nfEItz4XElyQ
```

Response
```
{
    "kind": "books#bookshelf",
    "id": 0,
    "title": "Favorites",
    "access": "PUBLIC",
    "updated": "2021-11-06T03:56:37.507Z",
    "created": "2021-11-06T03:56:37.507Z",
    "volumeCount": 5,
    "volumesLastUpdated": "2021-11-06T03:56:37.500Z"
}
```

## Consultar libros almacenados en una estantería especifica

Endpoint (http://localhost:8000/api/list-bookshelve/<user>/<bookshelve>/<key=ApiKey>).

Metodo GET

Reemplace <user> con el ID del usuario al que desea consultar la información y <bookshelve> con el numero de la estantería (los números de las estanterías publicas son 0,2,3,4) que desea consultar, además reemplace <key=ApiKey> por la apikey correspondiente, el body es vacío.

Request

```
http://localhost:8000/api/list-bookshelve/115859379337770019662/0/key=AIzaSyAKic6K3QaIGvl7wHLD8E4nfEItz4XElyQ
```

Response
```
[
    {
        "ID": "sZNKtwEACAAJ",
        "Titulo": "I Am Football",
        "Autor": [
            "Zlatan Ibrahimovic"
        ],
        "Editorial": "Viking"
    },
    {
        "ID": "qCIPEAAAQBAJ",
        "Titulo": "Maestro Fútbol",
        "Autor": [
            "Alexis García"
        ],
        "Editorial": "Intermedio Editores S.A.S"
    },
    {
        "ID": "BgHHAgAAQBAJ",
        "Titulo": "I Am Zlatan",
        "Autor": [
            "Zlatan Ibrahimovic"
        ],
        "Editorial": "Random House"
    }
]
```
## NOTA

Recuerde que el token de login tiene una duración de 60 minutos, luego se vencerá y deberá iniciar sesión de nuevo para seguir consultando los endpoints


el siguiente Response aparecera cuando intente entrar a un endpoint sin iniciar sesion o con el token vencido

```
{
    "detail":"Sin autenticar"
}
```