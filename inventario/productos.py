from inventario.bd import db

class Tramite(db.Model):
    __tablename__ = 'tramites'
    
    id = db.Column(db.Integer, primary_key=True)
    estudiante = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    costo = db.Column(db.Float, nullable=False)

    def __init__(self, estudiante, tipo, costo):
        self.estudiante = estudiante
        self.tipo = tipo
        self.costo = costo