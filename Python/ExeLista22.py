"""22 - Crie a classe Imóvel, que possui um endereço e um preço.
a. crie uma classe Novo, que herda Imóvel e possui um adicional no preço. Crie
métodos de acesso e impressão deste valor adicional.
b. crie uma classe Velho, que herda Imóvel e possui um desconto no preço. Crie
métodos de acesso e impressão para este desconto."""


class Imovel:
    def informacoes(self):
        self.endereco = input('Endereço do imóvel: ')

        while True:
            try:
                self.preco = float(input('Preço do imóvel: '))
                break

            except ValueError:
                print('Não é um valor válido!')


class Novo(Imovel):
    def adicional(self):
        super().informacoes()

        while True:
            try:
                adicional = float(input('Adicional do imóvel novo: '))
                break

            except ValueError:
                print('Não é um valor válido!')

        print('Endereço do imóvel: {}'.format(self.endereco))
        print('Valor do imóvel R$ {:.2f}'.format(self.preco))
        print('Valor adicional R$ {:.2f}'.format(adicional))
        print('Valor atualizado R$ {:.2f}'.format(self.preco + adicional))


class Velho(Imovel):
    def desconto(self):
        super().informacoes()

        while True:
            try:
                desconto = float(input('Desconto do imóvel velho: '))
                break

            except ValueError:
                print('Não é um valor válido!')

        print('Endereço do imóvel: {}'.format(self.endereco))
        print('Valor do imóvel R$ {:.2f}'.format(self.preco))
        print('Valor desconto R$ {:.2f}'.format(desconto))
        print('Valor atualizado R$ {:.2f}'.format(self.preco - desconto))


class Main:
    while True:
        print('Menu:\n'
              '1 - Imóvel novo\n'
              '2 - Imóvel velho\n'
              '3 - Sair')
        opcao = input('Digite a opção: ')

        if opcao == '1':
            novo = Novo()
            novo.adicional()

        elif opcao == '2':
            velho = Velho()
            velho.desconto()

        elif opcao == '3':
            exit()

        else:
            print('Opção inválida!')


if __name__ == '__main__':
    Main()
