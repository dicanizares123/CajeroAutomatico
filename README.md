Instalación del ambiente
Requerimientos
Python 3.10 o superior
PostgreSQL
Ubuntu Linux / MacOS
Instalación de gestor de ambientes virtuales de Python

sudo apt install python3-venv
Creación del ambiente virtual

python3 -m venv .venv
Activación del ambiente virtual

source .venv/bin/activate
Instalación de dependencias de este proyecto

pip3 install -r requirements.txt
En caso de querer desactivar el ambiente usar

deactivate
Windows
Instalación de gestor de ambientes virtuales de Python

pip install virtualenv
Creación del ambiente virtual

py -m venv .venv
Activación del ambiente virtual para CMD

.venv\Scripts\activate
Activación del ambiente virtual para PowerShell

.venv\Scripts\activate.ps1
Instalación de dependencias de este proyecto

pip install -r requirements.txt
En caso de querer desactivar el ambiente usar

deactivate
Comandos útiles
Iniciar servidor
Linux o MaCOS
python3 manage.py runserver
Windows
python manage.py runserver
Una vez inicializado el servidor se deberá dirigir al siguiente enlace: http://localhost:8000

Crear nueva aplicación
Linux o MaCOS
python3 manage.py startapp <nombre_de_la_aplicacion>
Windows
python manage.py startapp <nombre_de_la_aplicacion>
Crear Súper Usuario
Linux o MaCOS
python3 manage.py createsuperuser
Windows
python manage.py createsuperuser
Generar archivos de migración
Linux o MaCOS
python3 manage.py makemigrations
Windows
python manage.py makemigrations
Migrar a bases de datos
Linux o MaCOS
python3 manage.py migrate
Windows
python manage.py migrate
Almacenar dependencias y librerías instaladas
Linux o MaCOS
pip3 freeze > requirements.txt
Windows
pip freeze > requirements.txt
Nota

Ejemplos de Cadenas de Conexión para Django
PostgreSQL
Instalar pyscopg2
pip3 install psycopg2
Configurar archivo settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_tu_base_de_datos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
MySQL
Instalar mysqlclient
pip3 install mysqlclient
Configurar archivo settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_de_tu_base_de_datos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
SQLite
Configurar archivo settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
Oracle
Instalar cx_Oracle
pip3 install cx_Oracle
Configurar archivo settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'nombre_de_tu_base_de_datos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '1521',
    }
}
SQL Server (usando django-mssql-backend)
Instalar cx_Oracle
pip3 install django-mssql-backend
Configurar archivo settings.py
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'nombre_de_tu_base_de_datos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}
