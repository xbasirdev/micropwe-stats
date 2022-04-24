
# Instalando micro 2 (de estadisticas) (para linux)
## Previamente debes instalar y correr las migraciones del microservicio 1 que econtrara en el siguiente url https://github.com/XBasir/micropwe
### Pasos se intalacion

Abrir terminal y ejecutar siguientes comandos:

cd stats-pwe/

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

export FLASK_APP=stats-pwe.py

flask run
