from Conexao import ConectaMongo
from random import randint
from pprint import pprint


class Imoveis:

    def __init__(self):
        self.conexao = ConectaMongo()

    def gera_codigo(self):
        codigo = randint(100, 1000)
        return codigo

    def novo_imovel(self):
        codigo = self.gera_codigo()
        endereco = input('Endereço: ')
        numero = input('Número(caso ap pode usar letras): ')
        while True:
            try:
                valor = float(input('Valor: R$ '))
                if valor > 0:
                    break
                else:
                    print('Valor inválido!')

            except ValueError:
                print('Valor inválido!')

        imovel = {'codigo': codigo, 'endereco': endereco, 'numero': numero, 'valor': valor}
        self.conexao.salvar(imovel)

    def listar_imoveis(self):
        for itens in self.conexao.listar_todos():
            pprint(itens)
            print('-----------------------------')

    def listar_imovel(self):
        while True:

            try:
                codigo = int(input('Código do imóvel: '))
                break

            except ValueError:
                print('Código inválido!')

        pprint(self.conexao.listar_codigo({'codigo': codigo}))

    def remover_imovel(self):
        while True:

            try:
                codigo = int(input('Código do imóvel: '))
                break

            except ValueError:
                print('Código inválido!')

        self.conexao.remover({'codigo': codigo})
        print('Registro removido com sucesso!')
