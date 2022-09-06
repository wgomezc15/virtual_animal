# virtual_animal

Sistema de gestión para una veterinaria.


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


