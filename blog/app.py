from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return "Старт проекта FLASK! (POST)"
    elif request.method == 'GET':
        return "Старт проекта FLASK! (GET)"
    return "Работаем дальше."
