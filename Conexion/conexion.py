import mysql.connector

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='mysql-2d119ddc-uea-b69e.g.aivencloud.com',
            user='avnadmin',
            password='AVNS_XYJcQrtNUafY8HxHB-3',
            port=int(23611),
            database='defaultdb',
            ssl_disabled=False,
            ssl_verify_identity=False,
            use_pure=True
        )
        
        # LA SOLUCIÓN PARA AIVEN: Ajustar el nivel de seguridad de la transacción
        cursor = conexion.cursor()
        cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ")
        cursor.close()
        
        return conexion
    except Exception as e:
        print(f"🚨 ERROR CRÍTICO DE CONEXIÓN: {e}")
        return None