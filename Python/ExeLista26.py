#26 - Faça um programa que receba duas listas e retorne True se são iguais ou False caso contrário, além do número de ocorrências do primeiro elemento da lista.

lista1 = []
lista2 = []

print('Digite 5 elementos para a lista 1:')

for i in range(5):
    lista1.append(input('Elemento {}: '.format(i)))

print('Digite 5 elementos para a lista 2:')

for i in range(5):
    lista2.append(input('Elemento {}: '.format(i)))

if lista1 == lista2:
    print(True)
    print('O número de ocorrências do primeiro número da lista é: {}'.format(lista1.count(lista1[0])))

else:
    print(False)
