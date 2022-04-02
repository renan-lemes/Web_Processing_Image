from flask import Flask, render_template, request, jsonify, send_from_directory
import os

DIRECTION = "~/Area_de_Trabalho/Pojeto_/Web_Processing_Image/src/files"

app = Flask(__name__)

# linka uma url a uma função do python


@app.route("/", methods=["GET"])
def lista_arquivo():
    arquivos = []

    for nome_do_arquivo in os.listdir(DIRECTION):
        endereco_do_arquivo = os.path.join(DIRECTION, nome_do_arquivo)

        if(os.path.isfile(endereco_do_arquivo)):
            arquivos.append(nome_do_arquivo)

    return jsonify(arquivos)


@app.route('/')
def index():
    return render_template("index.html")
