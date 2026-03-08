import json
import csv
import os

CARPETA_ACTUAL = os.path.dirname(os.path.abspath(__file__))
CARPETA_DATA = os.path.join(CARPETA_ACTUAL, 'data')

# Asegurar que la carpeta data exista
if not os.path.exists(CARPETA_DATA):
    os.makedirs(CARPETA_DATA)

TXT_FILE = os.path.join(CARPETA_DATA, 'datos.txt')
JSON_FILE = os.path.join(CARPETA_DATA, 'datos.json')
CSV_FILE = os.path.join(CARPETA_DATA, 'datos.csv')

def guardar_en_archivos(estudiante, tipo, costo):
    # TXT
    with open(TXT_FILE, 'a', encoding='utf-8') as f:
        f.write(f"Estudiante: {estudiante} - Tramite: {tipo} - Costo: ${costo}\n")

    # JSON
    datos_json = []
    if os.path.exists(JSON_FILE) and os.path.getsize(JSON_FILE) > 0:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            datos_json = json.load(f)
            
    datos_json.append({"estudiante": estudiante, "tipo": tipo, "costo": costo})
    
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(datos_json, f, indent=4)

    # CSV
    archivo_existe = os.path.exists(CSV_FILE)
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        if not archivo_existe or os.path.getsize(CSV_FILE) == 0:
            escritor.writerow(['estudiante', 'tipo', 'costo'])
        escritor.writerow([estudiante, tipo, costo])

def leer_archivos():
    contenido_txt = []
    if os.path.exists(TXT_FILE):
        with open(TXT_FILE, 'r', encoding='utf-8') as f:
            contenido_txt = f.readlines()

    contenido_json = []
    if os.path.exists(JSON_FILE) and os.path.getsize(JSON_FILE) > 0:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            contenido_json = json.load(f)

    contenido_csv = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            lector = csv.reader(f)
            contenido_csv = list(lector)

    return contenido_txt, contenido_json, contenido_csv