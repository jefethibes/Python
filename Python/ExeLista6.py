"""6 - Faça um algoritmo que leia um nº inteiro e mostre uma mensagem indicando se este número é par ou ímpar, e se é positivo ou negativo"""

def par_ou_impar(numero):
    if numero % 2 == 0:
        print('Par!')

    else:
        print('Impar!')

def positivo_ou_negativo(numero):
    if numero >= 0:
        print('Positivo!')

    else:
        print('Negativo!')

while True:
    try:
        valor = int(input('Digite um número inteiro: '))
        break

    except ValueError:
        print('Digite apenas números inteiros!')

par_ou_impar(valor)
positivo_ou_negativo(valor)