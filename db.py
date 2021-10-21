import sqlite3
from sqlite3 import Error

db = 'database.db'

def conectar():
    try:
        conn= sqlite3.connect(db)
        print('Conectada a BDD')
        return conn
    except Error:
        print(Error)

def get_user(usuario):
    conn = conectar()
    cursor = conn.execute("select * from Usuarios where usuario = '"+ usuario + "';")
    resultSet = cursor.fetchone()
    conn.close()
    return resultSet

def add_user(nombre, apellido, correo, passw, usuario, rol):
    try :
        conn = conectar()
        conn.execute("insert into Usuarios (nombre, apellido, correo, password, usuario, rol) values (?,?,?,?,?,?);", (nombre, apellido, correo, passw, usuario, rol))
        conn.commit()
        conn.close()
        return True
    except Error:
        return False

def add_habitacion(nombre, descripcion, precio):
    try :
        conn = conectar()
        conn.execute("insert into Habitaciones (nombre, descripcion, precio) values (?,?,?);", (nombre, descripcion, precio))
        conn.commit()
        conn.close()
        return True
    except Error:
        return False


def add_reserva(id_usuario, personas, habitaciones, fecha_entrada, fecha_salida, dias, valor):
    try :
        conn = conectar()
        conn.execute("insert into Reservas (id_usuario, personas, habitaciones, fecha_entrada, fecha_salida, dias, valor_total) values (?,?,?,?,?,?,?);", (id_usuario, personas, habitaciones, fecha_entrada, fecha_salida, dias, valor))
        conn.commit()
        conn.close()
        return True
    except Error:
        return False

def add_detalle(id_habitacion, valor):
    try :
        conn = conectar()
        conn.execute("insert into DetalleReserva (id_habitacion, valor) values (?,?);", (id_habitacion, valor))
        conn.commit()
        conn.close()
        return True
    except Error:
        return False

def add_comentarios(codigo, calificacion, mensaje, id_usuario, bloqueo=0):
    try :
        conn = conectar()
        conn.execute("insert into Comentarios (codigo, calificacion, mensaje, id_usuario, bloqueo) values (?,?,?,?,?);", (codigo, calificacion, mensaje, id_usuario, bloqueo))
        conn.commit()
        conn.close()
        return True
    except Error:
        return False

def get_users():
    conn = conectar()
    cursor = conn.execute("select distinct usuario from Usuarios;")
    resultSet = cursor.fetchall()
    conn.close()
    users = [i[0] for i in resultSet]
    return users

def get_habitaciones():
    conn = conectar()
    cursor = conn.execute("select * from Habitaciones;")
    resultSet = cursor.fetchall()
    conn.close()
    return resultSet

def get_id_habitaciones():
    conn = conectar()
    cursor = conn.execute("select distinct id from Habitaciones;")
    resultSet = cursor.fetchall()
    conn.close()
    habitaciones = [i[0] for i in resultSet]
    return habitaciones

def get_habitacion(id):
    conn = conectar()
    cursor = conn.execute("select * from Habitaciones where id = "+ str(id) +";")
    resultSet = cursor.fetchone()
    conn.close()
    return resultSet

def get_reservas(id_usuario):
    conn = conectar()
    cursor = conn.execute("select * from Reservas where id_usuario = '"+ id_usuario +"';")
    resultSet = cursor.fetchall()
    conn.close()
    return resultSet
