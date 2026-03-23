from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from Conexion.conexion import obtener_conexion
from models import Usuario

app = Flask(__name__)
app.secret_key = 'clave_secreta_universitario_2026'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Por favor, inicie sesión para acceder al sistema."

@login_manager.user_loader
def load_user(user_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (user_id,))
    usuario_data = cursor.fetchone()
    conexion.close()
    
    if usuario_data:
        return Usuario(usuario_data['id_usuario'], usuario_data['nombre'], usuario_data['email'], usuario_data['password'])
    return None

# ==========================================
# RUTAS DE AUTENTICACIÓN
# ==========================================

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('inicio'))
        
    if request.method == 'POST':
        email = request.form['email']
        password_ingresada = request.form['password']
        
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        usuario_db = cursor.fetchone()
        conexion.close()
        
        if usuario_db and check_password_hash(usuario_db['password'], password_ingresada):
            usuario_obj = Usuario(usuario_db['id_usuario'], usuario_db['nombre'], usuario_db['email'], usuario_db['password'])
            login_user(usuario_obj)
            return redirect(url_for('inicio'))
        else:
            flash("Credenciales incorrectas. Verifique su correo y contraseña.")
            
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for('inicio'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password_plana = request.form['password']
        password_encriptada = generate_password_hash(password_plana)
        
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)", 
                           (nombre, email, password_encriptada))
            conexion.commit()
            flash("Usuario registrado exitosamente. Ahora puede iniciar sesión.")
            return redirect(url_for('login'))
        except Exception as e:
            flash("Error: El correo ingresado ya existe en el sistema.")
        finally:
            conexion.close()
            
    return render_template('registro.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# ==========================================
# RUTAS DEL SISTEMA (PROTEGIDAS)
# ==========================================

@app.route('/')
@login_required
def inicio():
    return render_template('index.html')

@app.route('/productos')
@login_required
def productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tramites")
    lista = cursor.fetchall()
    conexion.close()
    return render_template('productos.html', tramites=lista)

@app.route('/producto_form')
@login_required
def producto_form():
    tipos = ("Admisión", "Certificado", "Titulación", "Matrícula")
    return render_template('producto_form.html', tipos=tipos)

@app.route('/guardar', methods=['POST'])
@login_required
def guardar():
    estudiante = request.form['estudiante']
    tipo = request.form['tipo']
    costo = request.form['costo']
    
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO tramites (estudiante, tipo, costo) VALUES (%s, %s, %s)", (estudiante, tipo, costo))
    conexion.commit()
    conexion.close()
    return redirect(url_for('productos'))

@app.route('/eliminar_tramite/<int:id>')
@login_required
def eliminar_tramite(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM tramites WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()
    return redirect(url_for('productos'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)