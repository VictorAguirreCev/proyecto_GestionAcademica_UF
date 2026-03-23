import mysql.connector

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='mysql-2d119ddc-uea-b69e.g.aivencloud.com',
            user='avnadmin',
            password='AVNS_XYJcQrtNUafY8HxHB-3',
            port=int(23611),        # Forzamos matemáticamente el número
            database='defaultdb',
            ssl_disabled=False,
            ssl_verify_identity=False,
            use_pure=True           # SOLUCIÓN: Evita el colapso en Render
        )
        return conexion
    except Exception as e:
        print(f"🚨 ERROR CRÍTICO DE BASE DE DATOS: {e}")
        return None