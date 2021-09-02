from flask import Flask
import requests
import datetime

app = Flask(__name__)

url = "https://612db2b8e579e1001791dc8d.mockapi.io/api/v1/users"

get_result = requests.get(url)

@app.route("/usuarios")
def pegar_usuarios():
    get_json = get_result.json()
    users = []

    for i in get_json:
        users.append(i['name'])

    return str(users)

@app.route("/criado")
def pegar_datas_criacao():
    get_json = get_result.json()

    created = []

    for i in get_json:
        created.append(i['createdAt'])

    aux = datetime.datetime(created)
    return aux.strftime('%m/%d/%Y')