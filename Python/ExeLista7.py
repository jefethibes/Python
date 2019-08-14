"""7 - Escreva um algoritmo que leia 10 números informados pelo usuário e, depois, informe o menor,
número, o maior número, a soma dos números informados e a média aritmética dos números informados."""

numeros = []

while len(numeros) < 10:
    try:
        numeros.append(float(input('Digite um número: ')))

    except ValueError:
        print('Digite apenas números!')

print('O menor número digitado é {}'.format(min(numeros)))
print('O maior número digitado é {}'.format(max(numeros)))
print('A soma dos números digitados é {}'.format(sum(numeros)))
print('A média dos números digitados é {}'.format(sum(numeros) / len(numeros)))