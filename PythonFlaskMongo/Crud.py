from Conexao import ConectaMongo
from flask import Flask, request, jsonify


app = Flask(__name__)
conexao = ConectaMongo()


@app.route('/')
def inicio():
    return '######### Cadastro de Matriculas! #########'


@app.route('/cadastro', methods=['POST'])
def cadastra():
    data = request.json
    conexao.salvar(data)
    return 'Cadastrado!'


@app.route("/alterar/<int:id>", methods=['PUT'])
def atera(id):
    data = request.json
    return jsonify(conexao.alterar({'matricula': id}, data))


@app.route('/remover/<int:id>', methods=['DELETE'])
def deleta(id):
    return jsonify(conexao.deletar({'matricula': id}))


@app.route('/listar', methods=['GET'])
def consultar_todos():
    lista = []
    for itens in conexao.listar():
        lista.append(itens)

    return jsonify(lista)


@app.route('/consulta/<int:id>', methods=['GET'])
def consultar(id):
    return jsonify(conexao.consultar({'matricula': id}))
