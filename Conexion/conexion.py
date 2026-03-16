import mysql.connector

def obtener_conexion():
    conexion = mysql.connector.connect(
        host='mysql-2d119ddc-uea-b69e.g.aivencloud.com',
        user='avnadmin',
        password='AVNS_XYJcQrtNUafY8HxHB-3',
        port=23611,
        database='defaultdb',
        ssl_disabled=False,
        ssl_verify_identity=False
    )
    return conexion