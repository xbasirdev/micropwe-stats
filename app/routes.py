from flask import render_template, jsonify, make_response
from app import app, db
from app.models import Cuestionario

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
    return "ok"
