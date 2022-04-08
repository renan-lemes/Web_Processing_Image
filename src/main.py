from importlib.resources import path
from flask import Flask, render_template, request, jsonify, send_from_directory, Response
import os
import jyserver.Flask as jsf
#DIRECTION = "C:\\Users\\Renan Lemes\\OneDrive\\Área de Trabalho\\Projeto_\\Web_Processing_Image\\src\\assets"
DIRECTION = os.getcwd() + '/assets'

app = Flask(__name__)


@app.route("/assets", methods=["GET"])
def get_img():
    arquivos = []

    for nome_do_arquivo in os.listdir(DIRECTION):
        endereco_do_arquivo = os.path.join(DIRECTION, nome_do_arquivo)
        if(os.path.isfile(endereco_do_arquivo)):
            arquivos.append(nome_do_arquivo)
    return jsonify(arquivos)


@app.route("/assets/<nome_do_arquivo>", methods=["GET"])
def get_arquivo(nome_do_arquivo):
    return send_from_directory(DIRECTION, nome_do_arquivo, as_attachment=True)


@app.route("/assets", methods=["POST"])
def post_img():
    arquivo = request.files.get("meuArquivo")
    print(arquivo)
    nome_do_arquivo = arquivo.filename
    arquivo.save(os.path.join(DIRECTION, nome_do_arquivo))
    return Response(status=200)


""" 
@app.route('/', methods=["GET"])
def autenticar_img():
    img = request.args.get('nome_do_arquivo')
    print(img)
    return img """


@jsf.use(app)
class App:
    def __init__(self):
        arquivos = []
        for nome_do_arquivo in os.listdir(DIRECTION):
            endereco_do_arquivo = os.path.join(DIRECTION, nome_do_arquivo)
            if(os.path.isfile(endereco_do_arquivo)):
                arquivos.append(nome_do_arquivo)

        self.img = arquivos[0]
        print(self.img)

    def add_img(self):
        self.img = self.js.document.getElementBy(
            "ativar-img").innerHTML = self.img


@app.route('/')
def index():

    return App.render(render_template("index.html"))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
