# virtual_animal

Sistema de gestión para una veterinaria.



# Peticiones a la Api

*  CREATE USER

http://127.0.0.1:8000/user/

Request POST

```json
    {
        "username": "Alex",
        "password": "nomelase",
        "name": "Alexander",
        "lastname": "nomelase",
        "email": "alex@gmail.com",
        "typedocument": 1,
        "document": "1069583417",
        "telephone": "3118541236",
        "address": "Calle 183 #47 - 96",
        "gender": "M",
        "isactive": true
    }
```

*  LOGIN USER

http://127.0.0.1:8000/login/

Request POST

```json
    {
        "username": "Alex",
        "password": "nomelase"
    }
```

*  CREATE CLIENT

http://127.0.0.1:8000/client/

Request POS

```json
    {
        "name": "Josefina",
        "lastname": "Mesa",
        "email": "josefa@gmail.com",
        "document": "10256314",
        "typedocument": 2,
        "telephone": "3152542514",
        "address": "cll 25 #25-44",
        "gender": "F",
        "isactive": true
    }
```

*  CREATE PET

http://127.0.0.1:8000/pet/

Request POS

```json
    {
        "name": "Ruffo",
        "age": "7",
        "race": "gato malo",
        "sex": "M",
        "species": "gato",
        "features": "blanco con manchas negras",
        "isactive": true,
        "client": 10
    }
```

*  CREATE PETVACCINE

http://127.0.0.1:8000/petvaccine/

Request POS

```json
    {
        "pet":1,
        "vaccine":1,
        "fecha":"2022-09-27"
    }
```

*  CREATE CONSULTA

http://127.0.0.1:8000/consulta/

Request POS

```json
    {
        "motivo":"no come desde hace 2 días",
        "fecha":"2022-09-27",
        "peso":7.5,
        "ritmocardiaco": 150,
        "pet":1,
        "isactive": true
    }
```


# Configuración  de variables de entorno

* En la carpeta del proyecto *animalProject* agregar un archivo *.en* con la siguiente estructura, reemplazar los interrogantes
por los datos según corresponda:

DEBUG=True
SECRET_KEY=???
DB_DRIVER=django.db.backends.postgresql_psycopg2
DB_HOST=???
DB_PORT=5432
DB_NAME=???
DB_USER=???
DB_PASSWORD=???

# Notas

* Crea un entorno virtual

    python -m venv  env

* Activa entorno virtual

    env\Scripts\activate  // para windows
    source env/bin/activate //para linux

* Instala paquete django

    pip install django

* Crea el proyecto

    django-admin startproject nombre_del_proyecto

* Crea una aplicación

    django-admin startapp nombre_de_la_aplicacion

* Inicia la aplicación

    python manage.py runserver

* Instala paquete djangorestframework para crear una api rest

    pip install djangorestframework

* Instala paquete djangorestframework-simplejwt para autenticación con JWT

    pip install djangorestframework-simplejwt

* Instala paquete psycopg2 para conectar a base de datos postgresql
   
    pip install psycopg2

* Instala paquete python-decouple para separar la configuración y claves secretas de la aplicación en un archivo .env no
rastreado por Git.

    pib install python-decouple


# Comandos

* Actualiza pip (sistema de gestión de paquetes)

    python -m pip install --upgrade pip

*Genera o actualiza requirements.txt

    pip freeze > requirements.txt

*Instala requirements

    pip install -r requirements.txt

*Verifica paquetes desactualizados

    pip list --outdated

*Actualizar un paquete a la última versión

    pip install -U package_name


# Recursos

* pip

    https://pypi.org/project/pip/

* django

    https://pypi.org/project/Django/

* djangorestframework

    https://pypi.org/project/python-decouple/

* python-desacople

    https://pypi.org/project/python-decouple/

* djangorestframework-simplejwt

    https://pypi.org/project/djangorestframework-simplejwt/

* psycopg2

    https://pypi.org/project/psycopg2/