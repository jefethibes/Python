#25 - Faça uma função que receba uma lista e exiba os elementos da última metade na frente dos elementos da primeira metade

lista = []
nova_lista = []

print('Digite 10 elementos para uma lista: ')

for i in range(10):
    lista.append(input('Elemento {}: '.format(i)))

for i in range(5, 10, 1):
    nova_lista.append(lista[i])

for i in range(5):
    nova_lista.append(lista[i])

print('Lista: {}'.format(lista))
print('Lista com a última metade dos elementos na frente da primeira: {}'.format(nova_lista))
