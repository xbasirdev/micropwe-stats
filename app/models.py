from app import db

class Cuestionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), index=True, nullable=False)
    descripcion = db.Column(db.String(255), index=True, nullable=False)

class cuestionario_respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pregunta_id = db.Column(db.Integer)
    egresado_id = db.Column(db.Integer)
    respuesta = db.Column(db.String(255))
    fecha = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)