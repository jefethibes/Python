'''23 - Crie uma programa que recebe uma lista qualquer e:
a. retorne o maior elemento
b. retorne a soma dos elementos
c. retorne o número de ocorrências do primeiro elemento da lista
d. retorne a média dos elementos'''


lista = []

while True:
    try:
        lista.append(float(input('Digite um número: ')))

        opcao = input('Digite 1 para acrescentar main um número: ')
        if opcao != '1':
            break

    except ValueError:
        print('Digite apenas números!')


print('O maior número da lista é {}'.format(max(lista)))
print('A soma dos números da lista é {}'.format(sum(lista)))
print('O número de ocorrências do primeiro elemento da lista é {}'.format(lista.count(lista[0])))
print('A média dos elementos da lista é {}'.format(sum(lista) / len(lista)))
