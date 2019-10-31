from pymongo import MongoClient


class ConectaMongo:

    def __init__(self):
        try:
            self.mongo = MongoClient('localhost', 27017)
            self.banco = self.mongo.alunos
            self.colecao = self.banco.matriculas

        except Exception as e:
            print('Problema ao conectar!')
            print(e)

    def salvar(self, json):
        try:
            self.colecao.insert_one(json)

        except Exception as e:
            print('Problema ao salvar!')
            print(e)

    def listar(self, query=None):
        try:
            return self.colecao.find(query, {'_id': 0})

        except Exception as e:
            print('Problema ao listar!')
            print(e)

    def consultar(self, query):
        try:
            return self.colecao.find_one(query, {'_id': 0})

        except Exception as e:
            print('Problema ao consultar!')
            print(e)

    def deletar(self, query):
        try:
            self.colecao.remove(query)

        except Exception as e:
            print('Problema ao remover!')
            print(e)

    def alterar(self, query1, query2):
        try:
            self.colecao.update(query1, query2)

        except Exception as e:
            print('Problema ao atualizar!')
            print(e)
