from app import db

class Cuestionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), index=True, nullable=False)
    descripcion = db.Column(db.String(255), index=True, nullable=False)