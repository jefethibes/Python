"""9 - faça um método que receba um número X e uma palavra no console e repita x vezes a essa frase."""

while True:
    try:
        numero = int(input('Digite um número: '))
        break

    except ValueError:
        print('Digite apenas números inteiros!')

palavra = input('Digite um palavra: ')

for i in range(numero):
    print(palavra)