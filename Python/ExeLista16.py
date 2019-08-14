"""16 - Faça um algoritmo que leia os valores de COMPRIMENTO, LARGURA e ALTURA e apresente
o valor do volume de uma caixa retangular. Utilize para o cálculo a fórmula VOLUME = COMPRIMENTO * LARGURA * ALTURA."""

def volume(comprimento, largura, altura):
    print('O volume é {:.2f}'.format(comprimento * largura * altura))

def valores():
    print('Digite os valores:')
    while True:
        try:
            comprimento = float(input('Comprimento: '))
            largura = float(input('Largura: '))
            altura = float(input('Altura: '))
            break

        except ValueError:
            print('Digite apenas valores!')

    volume(comprimento, largura, altura)

valores()