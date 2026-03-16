from flask import Flask, render_template, request, redirect
from Conexion.conexion import obtener_conexion

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

# ==========================================
# CRUD: TABLA TRÁMITES
# ==========================================

@app.route('/productos')
def productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tramites")
    lista = cursor.fetchall()
    conexion.close()
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
    
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO tramites (estudiante, tipo, costo) VALUES (%s, %s, %s)", (estudiante, tipo, costo))
    conexion.commit()
    conexion.close()
    return redirect('/productos')

@app.route('/modificar_tramite', methods=['POST'])
def modificar_tramite():
    id_tramite = request.form['id']
    estudiante = request.form['estudiante']
    tipo = request.form['tipo']
    costo = request.form['costo']
    
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE tramites SET estudiante=%s, tipo=%s, costo=%s WHERE id=%s", (estudiante, tipo, costo, id_tramite))
    conexion.commit()
    conexion.close()
    return redirect('/productos')

@app.route('/eliminar_tramite/<int:id>')
def eliminar_tramite(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM tramites WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()
    return redirect('/productos')

# ==========================================
# CRUD: TABLA USUARIOS (Administrativos)
# ==========================================

@app.route('/usuarios')
def usuarios():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    lista_usuarios = cursor.fetchall()
    conexion.close()
    return render_template('usuarios.html', usuarios=lista_usuarios)

@app.route('/guardar_usuario', methods=['POST'])
def guardar_usuario():
    nombre = request.form['nombre']
    mail = request.form['mail']
    password = request.form['password']
    
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, mail, password) VALUES (%s, %s, %s)", (nombre, mail, password))
    conexion.commit()
    conexion.close()
    return redirect('/usuarios')

@app.route('/modificar_usuario', methods=['POST'])
def modificar_usuario():
    id_usuario = request.form['id_usuario']
    nombre = request.form['nombre']
    mail = request.form['mail']
    password = request.form['password']
    
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE usuarios SET nombre=%s, mail=%s, password=%s WHERE id_usuario=%s", (nombre, mail, password, id_usuario))
    conexion.commit()
    conexion.close()
    return redirect('/usuarios')

@app.route('/eliminar_usuario/<int:id>')
def eliminar_usuario(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (id,))
    conexion.commit()
    conexion.close()
    return redirect('/usuarios')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)