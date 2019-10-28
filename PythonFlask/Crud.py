from Conexao import ConectaSQL
from flask import Flask, request, jsonify


app = Flask(__name__)
conexao = ConectaSQL()


@app.route('/')
def inicio():
    return '######### Cadastro de Matriculas! #########'


@app.route('/cadastro', methods=['POST'])
def cadastra():
    data = request.json
    conexao.cadastrar(data)


@app.route("/minhaaplicacao/<int:id>", methods=['PUT'])
def atera(id):
    pass


@app.route('/minhaaplicacao/<int:id>', methods=['DELETE'])
def deleta(id):
    pass


@app.route('/minhaaplicacao', methods=['GET'])
def consultar():
    return 'teste'

