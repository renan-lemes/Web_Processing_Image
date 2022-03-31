from flask import Flask, render_template, request, jssonify, send_from_directory
import os 


app = Flask(__name__)

# linka uma url a uma função do python


@app.route('/')
def index():
    return render_template("index.html")
