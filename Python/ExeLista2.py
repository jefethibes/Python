"""2 - Escreva um algoritmo que solicita ao usuário para digitar um número inteiro positivo, e mostre-o por extenso.
Este número deverá variar entre 1 e 5. Se o usuário introduzir um número que não pertença a este intervalo,
mostre a frase “número inválido”."""

def numero():
    while True:
        try:
            n = int(input('Digite um número entre 1 e 5: '))
            if n > 0 and n < 6:
                break

        except ValueError:
            print('Número inválido!')

    if n == 1:
        print('Um!')

    elif n == 2:
        print('Dois!')

    elif n == 3:
        print('Três!')

    elif n == 4:
        print('Quatro!')

    else:
        print('Cinco!')

numero()