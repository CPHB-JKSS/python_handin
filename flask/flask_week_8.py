from flask import Flask, jsonify, request, abort
import json
import sqlalchemy as s_a
app = Flask(__name__)

#DB connection
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@db/week_8"
engine = s_a.create_engine(SQLALCHEMY_DATABASE_URL)
con = engine.connect()

@app.route('/')
def hello_world():
    return 'Hello, World! from python_handins flask_app2'

@app.route('/shakes')
def getAllShakes():
    query = "SELECT * from milkshakes"
    resultProxy = con.execute(query)
    resultSet = resultProxy.fetchall()

    return jsonify([dict(row) for row in resultSet])

@app.route('/shakes/add', methods=['POST'])
def addShake():

    #JSON DATA
    shake = {
    'flavor': request.json['flavor'],
    'size': request.json['size'],
    'price': request.json['price']
    }

    #FORM DATA
    #flavor = request.form.get('flavor'),
    #size = request.form.get('size'),
    #price = request.form.get('price')

    query = "INSERT INTO milkshakes(flavor, size, price) VALUES (%s, %s, %s)"
    con.execute(query, (shake['flavor'], shake['size'], shake['price']))

    return jsonify(shake)