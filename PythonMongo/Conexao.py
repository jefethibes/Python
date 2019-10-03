from pymongo import MongoClient


class ConectaMongo:

    def salvar(self, json):
        try:
            conexao = MongoClient('localhost', 27017)
            banco = conexao.imobiliaria
            novo_imovel = banco.imovel
            id = novo_imovel.insert_one(json).inserted_id
        except Exception as e:
            print('problema ao salvar registro')
            print(json)
            print(e)

    def listar_codigo(self, json):
        try:
            conexao = MongoClient('localhost', 27017)
            banco = conexao.imobiliaria
            listar = banco.imovel
            id = listar.find_one(json)
        except Exception as e:
            print('problema ao listar registro')
            print(json)
            print(e)

    def listar_todos(self):
        try:
            conexao = MongoClient('localhost', 27017)
            banco = conexao.imobiliaria
            litar = banco.imovel
            for itens in litar.find():
                print(itens)
        except Exception as e:
            print('problema ao listar registros')
            print(e)

    def remover(self, json):
        try:
            conexao = MongoClient('localhost', 27017)
            banco = conexao.imobiliaria
            remover = banco.imovel
            id = remover.remove(json)
        except Exception as e:
            print('problema ao remover registro')
            print(json)
            print(e)

    def alterar(self, json, novo_json):
        try:
            conexao = MongoClient('localhost', 27017)
            banco = conexao.imobiliaria
            altera = banco.imovel
            id = altera.update(json, novo_json)
        except Exception as e:
            print('problema ao alterar registro')
            print(json, novo_json)
            print(e)
