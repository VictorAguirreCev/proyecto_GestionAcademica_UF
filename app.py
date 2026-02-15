from flask import Flask

app = Flask(__name__)

def pagina_base(contenido):
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gestión Académica - UF</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background-color: #f4f7f6; }}
            .navbar {{ background-color: #003366; }} /* Azul institucional */
        </style>
    </head>
    <body>
        <nav class="navbar navbar-dark mb-4 shadow-sm">
            <div class="container">
                <a class="navbar-brand" href="/">🎓 Universitario de Formación</a>
            </div>
        </nav>
        <div class="container">
            {contenido}
        </div>
    </body>
    </html>
    """

# Ruta principal (Inicio)
@app.route('/')
def home():
    contenido = """
    <div class="p-5 mb-4 bg-white border rounded-3 shadow">
        <h1 class="display-5 fw-bold text-primary">Sistema de Gestión Académica y Bienestar</h1>
        <p class="col-md-10 fs-4 mt-3">Bienvenido a la plataforma central para la administración de posgrados y asistencia al estudiante.</p>
        <hr class="my-4">
        <p class="text-muted">Utilice las rutas del sistema para gestionar expedientes y solicitudes.</p>
        <a href="/estudiante/Victor" class="btn btn-primary btn-lg mt-2">Probar Ruta Dinámica</a>
    </div>
    """
    return pagina_base(contenido)

# Ruta dinámica (Perfil del estudiante)
@app.route('/estudiante/<nombre>')
def perfil_estudiante(nombre):
    contenido = f"""
    <div class="card shadow border-0">
        <div class="card-header bg-info text-white">
            <h4 class="mb-0">Expediente del Estudiante</h4>
        </div>
        <div class="card-body p-4">
            <h5 class="card-title display-6">Bienvenido, {nombre}</h5>
            <p class="card-text fs-5 mt-3">Tu solicitud de <strong>bienestar estudiantil</strong> y trámites de posgrado están en proceso de revisión.</p>
            <a href="/" class="btn btn-outline-secondary mt-3">Volver al Inicio</a>
        </div>
    </div>
    """
    return pagina_base(contenido)

if __name__ == '__main__':
    app.run(debug=True)