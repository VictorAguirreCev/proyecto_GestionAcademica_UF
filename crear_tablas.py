import mysql.connector

try:
    print("Conectando a la nube de Aiven...")
    conexion = mysql.connector.connect(
        host='mysql-2d119ddc-uea-b69e.g.aivencloud.com',
        user='avnadmin',
        password='AVNS_XYJcQrtNUafY8HxHB-3',
        port=23611,
        database='defaultdb',
        ssl_disabled=False,
        ssl_verify_identity=False
    )
    cursor = conexion.cursor()

    print("Creando tabla de usuarios...")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        mail VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL
    )
    """)

    print("Creando tabla de tramites...")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tramites (
        id INT AUTO_INCREMENT PRIMARY KEY,
        estudiante VARCHAR(100) NOT NULL,
        tipo VARCHAR(50) NOT NULL,
        costo DECIMAL(10,2) NOT NULL
    )
    """)
    
    conexion.commit()
    print("¡Éxito total! Tablas creadas en tu base de datos en la nube.")
    conexion.close()

except Exception as e:
    print(f"Ocurrió un error: {e}")