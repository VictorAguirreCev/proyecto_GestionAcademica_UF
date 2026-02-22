from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal (Inicio)
@app.route('/')
def home():
    return render_template('index.html')

# Ruta Acerca de (Requisito de la tarea)
@app.route('/about')
def about():
    return render_template('about.html')

# Ruta extra relacionada al negocio (Requisito de la tarea)
@app.route('/tramites')
def tramites():
    return render_template('tramites.html')

# Ruta dinámica (Perfil del estudiante)
@app.route('/estudiante/<nombre>')
def perfil_estudiante(nombre):
    # Pasamos la variable 'nombre' a la plantilla Jinja2
    return render_template('estudiante.html', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)