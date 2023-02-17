from flask import render_template, jsonify, make_response
from app import app, db
from app.models import Cuestionario, cuestionario_respuesta
import jsonpickle

@app.route('/')
@app.route('/index')
def index():
    entries = [
        {
            'id' : 1,
            'title': 'test title 1',
            'description' : 'test desc 1',
            'status' : True
        },
        {
            'id': 2,
            'title': 'test title 2',
            'description': 'test desc 2',
            'status': False
        }
    ]
    return render_template('index.html', entries=entries)

@app.route('/cuestionarios', methods=['GET'])
def cuestionarios():
    cuestionarios = Cuestionario.query.all()
    print(cuestionarios)
    return jsonpickle.encode(cuestionarios)

@app.route('/respuestas', methods=['GET'])
def respuestas():
    respuestas = cuestionario_respuesta.query.all()
    respuestas_list=[]
    respuesta_json = {}
    for respuesta in respuestas:
        respuesta_json = {
            "pregunta_id":respuesta.pregunta_id,
            "egresado_id":respuesta.egresado_id,
            "respuesta":respuesta.respuesta,
            "fecha":respuesta.fecha,
            "created_at":respuesta.created_at
        }
        respuestas_list.append(respuesta_json)
    response = jsonify(respuestas_list)
    return response