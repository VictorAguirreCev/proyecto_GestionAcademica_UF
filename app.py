from flask import Flask, render_template, request, redirect
import os

from form import ValidadorFormulario
from inventario.bd import db
from inventario.productos import Tramite
from inventario.inventario import guardar_en_archivos, leer_archivos

app = Flask(__name__)

CARPETA_RAIZ = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(CARPETA_RAIZ, 'universidad.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')

@app.route('/productos')
def productos():
    lista = Tramite.query.all()
    return render_template('productos.html', tramites=lista)

@app.route('/producto_form')
def producto_form():
    tipos = ("Admisión", "Certificado", "Titulación", "Matrícula")
    return render_template('producto_form.html', tipos=tipos)

@app.route('/guardar', methods=['POST'])
def guardar():
    estudiante = request.form['estudiante']
    tipo = request.form['tipo']
    costo = request.form['costo']

    if ValidadorFormulario.validar_tramite(estudiante, tipo, costo):
        nuevo_registro = Tramite(estudiante, tipo, float(costo))
        db.session.add(nuevo_registro)
        db.session.commit()

        guardar_en_archivos(estudiante, tipo, float(costo))

    return redirect('/productos')

@app.route('/datos')
def datos():
    txt, json_data, csv_data = leer_archivos()
    return render_template('datos.html', txt=txt, json=json_data, csv=csv_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)