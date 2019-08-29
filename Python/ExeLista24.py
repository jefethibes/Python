'''24 - Receba duas listas e exiba a união destas listas e a intercalação destas listas,
isto é, 1º da 1ª lista, 1º da 2ª lista, 2º da 1ª lista, 2º da 2ª lista.'''


lista1 = []
lista2 = []
lista_intercalada = []

print('Digite 5 elementos para a lista 1:')

for i in range(5):
    lista1.append(input('Elemento {}: '.format(i)))

print('Digite 5 elementos para a lista 2:')

for i in range(5):
    lista2.append(input('Elemento {}: '.format(i)))

print('A união das listas: {}'.format(lista1 + lista2))

for i, x in zip(lista1, lista2):
    lista_intercalada.append(i)
    lista_intercalada.append(x)

print('Lista intercalada: {}'.format(lista_intercalada))
