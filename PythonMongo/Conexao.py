from pymongo import MongoClient


class ConectaMongo:

    def __init__(self):
        try:
            self.mongo = MongoClient('localhost', 27017)
            self.banco = self.mongo.imobiliaria
            self.colecao = self.banco.imovel
        except Exception as e:
            print('Problema ao conectar no banco!')
            print(e)

    def salvar(self, json):
        try:
            self.colecao.insert_one(json)
        except Exception as e:
            print('Problema ao salvar registro!')
            print(json)
            print(e)

    def listar_todos(self, query=None):
        try:
            return self.colecao.find(query, {'_id': 0})
        except Exception as e:
            print('Problema ao listar registros!')
            print(e)

    def listar_codigo(self, json):
        try:
            return self.colecao.find_one(json, {'_id': 0})
        except Exception as e:
            print('Problema ao listar registro!')
            print(json)
            print(e)

    def remover(self, json):
        try:
            self.colecao.remove(json)
        except Exception as e:
            print('Problema ao remover registro!')
            print(json)
            print(e)
