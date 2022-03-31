from flask import Flask, render_template

app = Flask(__name__)

# linka uma url a uma função do python


@app.route('/')
def index():
    return render_template("index.html")
