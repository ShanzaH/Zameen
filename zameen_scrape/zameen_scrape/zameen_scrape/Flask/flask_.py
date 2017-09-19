from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:arbisoft123@localhost/scrapy'
app.debug = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

#@app.route('/')
#def homepage():
#    return render_template("main.html")


@app.route('/', methods=['POST','GET'])
def search():
    if request.method == "GET":

        return jsonify()
