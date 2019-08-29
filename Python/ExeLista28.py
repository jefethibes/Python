'''28 - Faça um programa que percorre uma lista e exiba na tela o valor mais próximo da média dos valores da lista.
Exemplo: lista = [2.5, 7.5, 10.0, 4.0] (média = 6.0). Valor mais próximo da média = 7.5'''


lista = []

while True:
    try:
        lista.append(float(input('Digite um número para adicionar na lista: ')))
        opcao = input('Se deseja adicionar mais um valor digite 1 caso não digite qualquer outra tecla: ')
        if opcao != '1':
            break

    except ValueError:
        print('Digite apenas números!')


media = sum(lista) / len(lista)
maior_elemento = max(lista)

if media in lista:
    print('Valor mais próximo da média: {}'.format(media))

else:
    for i in range(len(lista)):
        if media - lista[i] < maior_elemento:
            maior_elemento = lista[i]

    print('Valor mais próximo da média: {}'.format(maior_elemento))