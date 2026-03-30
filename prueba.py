import pymysql

print("Intentando conectar a Aiven con PyMySQL...")

try:
    conexion = pymysql.connect(
        host='mysql-2d119ddc-uea-b69e.g.aivencloud.com',
        user='avnadmin',
        password='AVNS_XYJcQrtNUafY8HxHB-3',
        port=23611,
        database='defaultdb'
    )
    print("¡ÉXITO TOTAL! La puerta está abierta.")
    conexion.close()

except Exception as e:
    print("=====================================")
    print("LA PUERTA ESTÁ CERRADA. EL MOTIVO ES:")
    print(e)
    print("=====================================")