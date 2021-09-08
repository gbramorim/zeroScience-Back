from flask import Flask
import flask
import requests
from requests.api import get, request

app = Flask(__name__)

url = "https://612db2b8e579e1001791dc8d.mockapi.io/api/v1/users"

get_result = requests.get(url)


@app.route("/usuarios")
def pegar_usuarios():
    get_json = get_result.json()
    main_user = []

    # http://127.0.0.1:5000/usuarios?nome=Denise%20Davis for tests
    user = flask.request.args.get("nome")

    for i in get_json:
        if i['name'] == user:
            main_user.append(user)
        # else:
        #     main_user.append("Não!")

    return str(main_user)

# @app.route("/criado")
# def pegar_datas_criacao():
#     get_json = get_result.json()
#     # h = get_json[1]
#     n

#     for i in get_json:
#         created.append(i['createdAt'])

#     return str(created)
