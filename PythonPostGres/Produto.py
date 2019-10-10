from Conexao import ConectaSQL
from random import randint


class Produtos:

    def __init__(self):
        self.conecta_sql = ConectaSQL()

    def gera_cod(self):
        return randint(0, 5000)

    def novo_produto(self):
        cod = self.gera_cod()
        nome = input('Nome produto: ')

        while True:
            try:
                preco = float(input('Preço: '))
                if preco > 0:
                    break
                else:
                    print('Valor inválido!')

            except ValueError:
                print('Valor inválido!')

        self.conecta_sql.salvar_produto(cod, nome, preco)

    def deletar(self):
        try:
            codigo = int(input('Digite o cod do produto que deseja remover: '))
            self.conecta_sql.deletar_produto(codigo)
        except ValueError:
            print('Código inválido!')

    def listar_todos(self):
        aux = self.conecta_sql.listar_produtos('select * from produtos')
        for produto in aux:
            print('Código: {}'.format(produto[0]))
            print('Nome: {}'.format(produto[1]))
            print('Preço: R$ {}'.format(produto[2]))
            print('--------------------')

    def listar(self):
        cod = int(input('Código do produto: '))
        aux = self.conecta_sql.listar_produto('select * from produtos where cod_produto = {}'.format(cod))
        print('Cóodigo: {}'.format(aux[0][0]))
        print('Nome: R$ {}'.format(aux[0][1]))
        print('Preço: R$ {}'.format(aux[0][2]))
        print('-------------------------')

    def alterar(self):
        cod = int
        preco = float

        try:
            cod = int(input('Digite o codigo do produto: '))
        except ValueError:
            print('Valor inválido!')

        nome = input('Novo nome: ')

        try:
            preco = float(input('Novo preço: R$ '))
        except ValueError:
            print('Valor inválido!')

        self.conecta_sql.atualizar_produto(nome, preco, cod)
