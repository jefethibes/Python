"""11 -  Escreva um algoritmo para ler um valor (do teclado) e escrever (na tela) o seu antecessor."""

while True:
    try:
        valor = int(input('Digite um número inteiro: '))
        break

    except ValueError:
        print('Digite apenas números inteiros!')

print('O número que antecede {} é {}'.format(valor, valor - 1))