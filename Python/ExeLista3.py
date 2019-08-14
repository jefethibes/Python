"""3 - Crie uma classe calculadora com as quatro operações básicas (soma, subtração, multiplicação e divisão).
O usuário deve informar dois números e o programa deve fazer as quatro operações. (modifique para calcular
tudo no mesmo método, somando 1 ao resultado de cada operação)"""

class Operacoes:
    def soma(self, n1, n2):
        print('A soma dos números é {}'.format(n1 + n2))

    def subtracao(self, n1, n2):
        print('A subtração dos números é {}'.format(n1 - n2))

    def multiplicacao(self, n1, n2):
        print('A multiplicação dos números é {}'.format(n1 * n2))

    def divisao(self, n1, n2):
        print('A divisão dos números é {}'.format(n1 / n2))

while True:
    try:
        N1 = int(input('Digite um número inteiro: '))
        break

    except ValueError:
        print('Digite apenas números inteiros!')

while True:
    try:
        N2 = int(input('Digite outro número inteiro: '))
        break

    except ValueError:
        print('Digite apenas números inteiros!')

op = Operacoes()

op.soma(N1, N2)
op.subtracao(N1, N2)
op.multiplicacao(N1, N2)
op.divisao(N1, N2)