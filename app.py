from flask import Flask
import requests


app = Flask(__name__)

#URL Mockada para consultas é só alterar
url = "https://612db2b8e579e1001791dc8d.mockapi.io/api/v1/users"

x = requests.get(url)

@app.route("/")

def hello_world():
    return x.text

