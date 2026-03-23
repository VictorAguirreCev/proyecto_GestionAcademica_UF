import mysql.connector

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='mysql-2d119ddc-uea-b69e.g.aivencloud.com',
            user='avnadmin',
            password='AVNS_XYJcQrtNUafY8HxHB-3',
            port=23611,
            database='defaultdb',
            ssl_disabled=False,
            ssl_verify_identity=False,
            connect_timeout=10
        )
        return conexion
    except Exception as e:
        # Esto imprimirá el error exacto en la consola de Render
        print(f"🚨 ERROR CRÍTICO DE BASE DE DATOS: {e}")
        return None