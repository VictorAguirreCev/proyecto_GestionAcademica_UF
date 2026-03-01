from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# --- PROGRAMACIÓN ORIENTADA A OBJETOS (POO) ---

# Clase para el objeto individual (Producto/Trámite)
class Tramite:
    def __init__(self, id, estudiante, tipo, costo):
        self.id = id
        self.estudiante = estudiante
        self.tipo = tipo
        self.costo = costo

# Clase para el Inventario y Base de Datos
class GestionInventario:
    def __init__(self):
        # COLECCIÓN: Diccionario para manejar datos en memoria
        self.mis_datos = {}
        self.crear_tabla()

    def conectar(self):
        return sqlite3.connect("inventario.db")

    def crear_tabla(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS registros 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           estudiante TEXT, tipo TEXT, costo REAL)''')
        conexion.commit()
        conexion.close()

    def agregar(self, e, t, c):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO registros (estudiante, tipo, costo) VALUES (?, ?, ?)", (e, t, c))
        conexion.commit()
        conexion.close()

    def listar(self):
        conexion = self.conectar()
        conexion.row_factory = sqlite3.Row
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM registros")
        filas = cursor.fetchall()
        conexion.close()
        
        # Llenamos el diccionario (Colección)
        self.mis_datos.clear()
        for f in filas:
            nuevo = Tramite(f['id'], f['estudiante'], f['tipo'], f['costo'])
            self.mis_datos[f['id']] = nuevo
        return self.mis_datos

    def borrar(self, id_borrar):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM registros WHERE id = ?", (id_borrar,))
        conexion.commit()
        conexion.close()

# Instancia manual del gestor
inventario = GestionInventario()

# --- RUTAS DE LA APLICACIÓN ---

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/about')
def acerca():
    return render_template('about.html')

@app.route('/gestion')
def pantalla_gestion():
    # COLECCIÓN: Tupla para opciones fijas
    opciones = ("Admisión", "Certificado", "Titulación", "Matrícula")
    datos = inventario.listar()
    return render_template('gestion_tramites.html', lista=datos.values(), tipos=opciones)

@app.route('/enviar_datos', methods=['POST'])
def enviar_datos():
    est = request.form['estudiante']
    tip = request.form['tipo']
    cos = request.form['costo']
    inventario.agregar(est, tip, cos)
    return redirect('/gestion')

@app.route('/quitar/<int:id_reg>')
def quitar(id_reg):
    inventario.borrar(id_reg)
    return redirect('/gestion')

if __name__ == '__main__':
    app.run(debug=True)