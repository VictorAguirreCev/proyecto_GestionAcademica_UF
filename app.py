from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ==========================================
# 1. CLASES (POO)
# ==========================================
class Tramite:
    def __init__(self, id_tramite, estudiante, tipo, costo):
        self.id = id_tramite
        self.estudiante = estudiante
        self.tipo = tipo
        self.costo = costo

class InventarioTramites:
    def __init__(self, nombre_db='universidad.db'):
        self.nombre_db = nombre_db
        self.crear_tabla()

    def conectar(self):
        return sqlite3.connect(self.nombre_db)

    def crear_tabla(self):
        conexion = self.conectar()
        conexion.execute('''CREATE TABLE IF NOT EXISTS tramites 
                           (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            estudiante TEXT, tipo TEXT, costo REAL)''')
        conexion.commit()
        conexion.close()

    def agregar(self, estudiante, tipo, costo):
        conexion = self.conectar()
        conexion.execute("INSERT INTO tramites (estudiante, tipo, costo) VALUES (?, ?, ?)", 
                         (estudiante, tipo, costo))
        conexion.commit()
        conexion.close()

    def listar_todos(self):
        conexion = self.conectar()
        conexion.row_factory = sqlite3.Row
        filas = conexion.execute("SELECT * FROM tramites").fetchall()
        conexion.close()
        
        # COLECCIÓN: Diccionario para almacenar los objetos
        diccionario_tramites = {}
        for fila in filas:
            diccionario_tramites[fila['id']] = Tramite(fila['id'], fila['estudiante'], fila['tipo'], fila['costo'])
        return diccionario_tramites

    def eliminar(self, id_borrar):
        conexion = self.conectar()
        conexion.execute("DELETE FROM tramites WHERE id = ?", (id_borrar,))
        conexion.commit()
        conexion.close()

# Instancia global
gestor = InventarioTramites()

# ==========================================
# 2. RUTAS WEB
# ==========================================
@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/about')
def acerca_de():
    return render_template('about.html')

@app.route('/gestion')
def gestion():
    # COLECCIÓN: Tupla con los tipos de trámites válidos
    tipos_validos = ("Admisión", "Certificado", "Titulación", "Matrícula")
    datos = gestor.listar_todos()
    return render_template('gestion_tramites.html', tramites=datos.values(), tipos=tipos_validos)

@app.route('/guardar', methods=['POST'])
def guardar():
    est = request.form['estudiante']
    tip = request.form['tipo']
    cos = request.form['costo']
    gestor.agregar(est, tip, cos)
    return redirect('/gestion')

@app.route('/borrar/<int:id_tramite>')
def borrar(id_tramite):
    gestor.eliminar(id_tramite)
    return redirect('/gestion')

if __name__ == '__main__':
    # El host='0.0.0.0' ayuda a evitar problemas de puertos en algunos entornos
    app.run(host='0.0.0.0', port=5000, debug=True)