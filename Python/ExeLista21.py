"""Crie uma classe chamada Ingresso que possui um valor em reais e um método
imprimeValor().
a. crie uma classe VIP, que herda Ingresso e possui um valor adicional. Crie um
método que retorne o valor do ingresso VIP (com o adicional incluído).
b. crie uma classe Normal, que herda Ingresso e possui um método que imprime:
"Ingresso Normal".
c. crie uma classe CamaroteInferior (que possui a localização do ingresso e métodos
para acessar e imprimir esta localização) e uma classe CamaroteSuperior, que é
mais cara (possui valor adicional). Esta última possui um método para retornar o
valor do ingresso. Ambas as classes herdam a classe VIP"""


class Ingresso:
    def __init__(self):
        self.valor_ingresso = float
        self.valor_adicional = float

    def imprime_valor(self):
        while True:
            try:
                self.valor_ingresso = float(input('Valor do ingresso: '))
                break
            except ValueError:
                print('Não é um valor válido!')

        print('Valor do ingresso: R$ {:.2f}'.format(self.valor_ingresso))


class Vip(Ingresso):
    def add_valor(self):
        super().imprime_valor()
        while True:
            try:
                self.valor_adicional = float(input('Valor adicional: '))
                break

            except ValueError:
                print('Não é um valor válido!')

        print('Valor adicional: R$ {:.2f}'.format(self.valor_adicional))
        print('Valor Total: R$ {:.2f}'.format(self.valor_ingresso + self.valor_adicional))


class Normal(Ingresso):
    def ingresso_normal(self):
        print('Ingresso Normal!')
        super().imprime_valor()
        print('----------------')


class CamaroteInferior(Vip):
    def localizacao(self):
        print('Camarote Inferior!')
        super().add_valor()
        print('------------------')


class CamaroteSuperior(Vip):
    def localizacao(self):
        print('Camarote Superior!')
        super().add_valor()
        print('------------------')


def Main():
    normal = Normal()
    camarote_inferior = CamaroteInferior()
    camarote_superior = CamaroteSuperior()

    normal.ingresso_normal()
    camarote_inferior.localizacao()
    camarote_superior.localizacao()


if __name__ == '__main__':
    Main()
