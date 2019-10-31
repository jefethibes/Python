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
    return 'Cadastrado com sucesso!'


@app.route("/alterar/<int:id>", methods=['PUT'])
def altera(id):
    data = request.json
    conexao.alterar(id, data)
    return 'Alterado com sucesso!'


@app.route('/remover/<int:id>', methods=['DELETE'])
def deleta(id):
    conexao.deletar(id)
    return 'Removido com sucesso!'


@app.route('/listar', methods=['GET'])
def listar():
    aux = []
    for itens in conexao.listar_todos():
        aux.append(itens)

    return jsonify(aux)


@app.route('/consulta/<int:id>', methods=['GET'])
def consultar(id):
    aux = []
    aux.append(conexao.consulta(id))

    return jsonify(aux)
