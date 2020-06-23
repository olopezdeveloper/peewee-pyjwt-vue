"""Este Archivo Crea la Base de datos SQLite y agrega dos usuarios de prueba"""
import sqlite3
import os
from sqlite3 import Error
from api.settings_secret import DATABASES_NAME
from api.models import User, Note
from peewee import SqliteDatabase, OperationalError, IntegrityError


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    path = os.path.abspath('')
    create_connection("{path}/{name}".format(path=path, name=DATABASES_NAME))

    db = SqliteDatabase(DATABASES_NAME)

    # Creacion de las tablas en Base de Datos
    try:
        db.create_tables([User, Note])
    except OperationalError as e:
        print("Tables User and Note Already exist")
    except Error as e:
        print(e)

    # Validacion si admin ya existe
    try:
        user = User(username="admin", password="123456")
        user.save()
    except IntegrityError as e:
        print("User 'admin' ya existe")
    except Error as e:
        print(e)

    try:
        user = User(username="super", password="123456")
        user.save()
    except IntegrityError as e:
        print("User 'super' ya existe")
    except Error as e:
        print(e)

    print("Success!")
