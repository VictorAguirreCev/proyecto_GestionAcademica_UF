from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

class Tramite:
    """Clase que representa un ítem individual en el sistema (Equivalente a 'Producto')."""
    def __init__(self, id_tramite, estudiante, tipo, costo):
        self.id = id_tramite
        self.estudiante = estudiante
        self.tipo = tipo
        self.costo = costo

class GestorTramites:
    """Clase para gestionar la conexión a SQLite y las colecciones de datos."""
    def __init__(self, db_name='universidad.db'):
        self.db_name = db_name
        # USO DE COLECCIONES: Un conjunto (Set) para búsquedas rápidas de categorías válidas.
        self.tipos_validos = {"Admisión", "Certificado", "Titulación", "Matrícula"}
        self.inicializar_db()

    def conectar(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row # Permite manejar los registros como diccionarios
        return conn

    def inicializar_db(self):
        """Crea la tabla si no existe en la base de datos SQLite."""
        conn = self.conectar()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tramites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                estudiante TEXT NOT NULL,
                tipo TEXT NOT NULL,
                costo REAL NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def agregar(self, tramite):
        """CRUD: Create"""
        conn = self.conectar()
        conn.execute('INSERT INTO tramites (estudiante, tipo, costo) VALUES (?, ?, ?)',
                     (tramite.estudiante, tramite.tipo, tramite.costo))
        conn.commit()
        conn.close()

    def obtener_todos(self):
        """CRUD: Read. USO DE COLECCIONES: Retorna un Diccionario de objetos Tramite."""
        conn = self.conectar()
        filas = conn.execute('SELECT * FROM tramites').fetchall()
        conn.close()
        
        # Colección: Diccionario usando el ID como clave para acceso eficiente O(1)
        diccionario_tramites = {}
        for fila in filas:
            diccionario_tramites[fila['id']] = Tramite(fila['id'], fila['estudiante'], fila['tipo'], fila['costo'])
        return diccionario_tramites

    def actualizar(self, id_tramite, tipo, costo):
        """CRUD: Update"""
        conn = self.conectar()
        conn.execute('UPDATE tramites SET tipo = ?, costo = ? WHERE id = ?', (tipo, costo, id_tramite))
        conn.commit()
        conn.close()

    def eliminar(self, id_tramite):
        """CRUD: Delete"""
        conn = self.conectar()
        conn.execute('DELETE FROM tramites WHERE id = ?', (id_tramite,))
        conn.commit()
        conn.close()

# Instanciar el gestor globalmente
gestor = GestorTramites()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Submenú principal del CRUD
@app.route('/gestion_tramites')
def gestion_tramites():
    # Obtener el diccionario de trámites desde SQLite
    diccionario_tramites = gestor.obtener_todos()
    # Convertir los valores del diccionario a una lista para enviarlos a la plantilla Jinja2
    lista_tramites = list(diccionario_tramites.values())
    return render_template('gestion_tramites.html', tramites=lista_tramites, tipos=gestor.tipos_validos)

@app.route('/agregar', methods=['POST'])
def agregar_tramite():
    estudiante = request.form['estudiante']
    tipo = request.form['tipo']
    costo = float(request.form['costo'])
    nuevo_tramite = Tramite(None, estudiante, tipo, costo)
    gestor.agregar(nuevo_tramite)
    return redirect(url_for('gestion_tramites'))

@app.route('/eliminar/<int:id>')
def eliminar_tramite(id):
    gestor.eliminar(id)
    return redirect(url_for('gestion_tramites'))

@app.route('/actualizar', methods=['POST'])
def actualizar_tramite():
    id_tramite = request.form['id']
    nuevo_tipo = request.form['tipo']
    nuevo_costo = float(request.form['costo'])
    gestor.actualizar(id_tramite, nuevo_tipo, nuevo_costo)
    return redirect(url_for('gestion_tramites'))

if __name__ == '__main__':
    app.run(debug=True)