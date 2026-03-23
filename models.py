from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, id_usuario, nombre, email, password):
        self.id = str(id_usuario)  # Flask-Login requiere que el ID sea string y se llame 'id'
        self.nombre = nombre
        self.email = email
        self.password = password