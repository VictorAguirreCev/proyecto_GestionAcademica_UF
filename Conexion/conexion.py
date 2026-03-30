import pymysql

def obtener_conexion():
    try:
        conexion = pymysql.connect(
            host='mysql-2d119ddc-uea-b69e.g.aivencloud.com',
            user='avnadmin',
            password='AVNS_XYJcQrtNUafY8HxHB-3',
            port=23611,
            database='defaultdb'
        )
        
        # Ajuste estricto para que Aiven permita registrar usuarios sin fallar
        cursor = conexion.cursor()
        cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ")
        cursor.close()
        
        return conexion
    except Exception as e:
        print(f"🚨 ERROR CRÍTICO DE CONEXIÓN: {e}")
        return None