from distutils.log import debug
from flask import Flask, render_template, request, jsonify, send_from_directory
import os

DIRECTION = "C:\\Users\\Renan Lemes\\OneDrive\\Área de Trabalho\\Projeto_\\Web_Processing_Image\\src\\files"

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


@app.route("/<nome_do_arquivo>", methods=["POST"])
def get_arquivo(nome_do_arquivo):
    return send_from_directory(DIRECTION, nome_do_arquivo, as_attachment=True)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
    render_template("index.html")
