import psycopg2


class ConectaSQL:

    def __init__(self):
        try:
            self.conexao = psycopg2.connect(user='postgres',
                                            password='ads',
                                            host='127.0.0.1',
                                            port='5432',
                                            database='supermercado')
            self.conexao.autocommit = True
            self.cursor = self.conexao.cursor()
        except Exception as e:
            print('Erro ao conectar!')
            print(e)

    def salvar_produto(self, cod, nome, preco):
        try:
            self.cursor.execute("Insert into produtos (cod_produto, nome, preco) values ({}, '{}', {});"
                                .format(cod, nome, preco))
        except Exception as e:
            print('Erroa ao salvar!')
            print(e)

    def deletar_produto(self, cod):
        try:
            self.cursor.execute('Delete from produtos where cod_produto = {};'.format(cod))
            print('Produto removido com sucesso!')
        except Exception as e:
            print('Erro ao remover!')
            print(e)

    def listar_produtos(self, query):
        try:
            aux = self.cursor.execute(query)
            aux = self.cursor.fetchall()
            return aux
        except Exception as e:
            print('Erro ao listar!')
            print(e)

    def listar_produto(self, query):
        try:
            aux = self.cursor.execute(query)
            aux = self.cursor.fetchall()
            return aux
        except Exception as e:
            print('Erro ao listar!')
            print(e)

    def atualizar_produto(self, nome, preco, cod_produto):
        try:
            self.cursor.execute("update produtos set nome = '{}', preco = {} where cod_produto = {};"
                                .format(nome, preco, cod_produto))
        except Exception as e:
            print('Erro ao atualiza!')
            print(e)
