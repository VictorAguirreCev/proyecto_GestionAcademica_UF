import mysql.connector

def obtener_conexion():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='gestion_academica'
    )
    return conexion