from pymongo import MongoClient
from bson.objectid import ObjectId


class Conexao:

    def __init__(self):
        try:
            self.conexao = MongoClient('localhost', 27017)
            self.base = self.conexao.suporte
        except Exception as e:
            print(e)

    def chamados(self, col, json):
        try:
            colecao = self.base[col]
            colecao.insert_one(json)
        except Exception as e:
            print(e)

    def valida_login(self, json):
        try:
            colecao = self.base.usuarios
            return colecao.find_one(json)
        except Exception as e:
            print(e)

    def busca_administracao(self, query=None):
        try:
            colecao = self.base.administracao
            return colecao.find_one(query)
        except Exception as e:
            print(e)

    def meus_chamados(self, col=None):
        try:
            colecao = self.base[col]
            return colecao.find()
        except Exception as e:
            print(e)

    def encerrar_chamado(self, col, _id, query):
        try:
            colecao = self.base[col]
            colecao.update({'_id': ObjectId(_id)}, query)
        except Exception as e:
            print(e)

    def busca_chamado(self, col, query):
        try:
            colecao = self.base[col]
            return colecao.find_one({'_id': ObjectId(query)})
        except Exception as e:
            print(e)

    def valida_permissao(self, user):
        try:
            colecao = self.base.usuarios
            aux = colecao.find_one({'usuario': user})
            return aux['permissao']
        except Exception as e:
            print(e)