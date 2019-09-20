'''Escreva um programa que receba do usuário 5 números inteiros e o nome do arquivo no qual eles devem
ser armazenados. Em seguida, ler do arquivo estes valores armazenados copiando-os para um vetor
de inteiros e imprimindo na tela.'''


armazena_numeros = []
aux = 1

nome_arquivo = input('Digite o nome do arquivo que deseja armazenar os números: ')

numeros = open('C:\\WorkSpace\\' + nome_arquivo + '.txt', 'w')

while aux <= 5:
    try:
        novo_numero = int(input('Digite um número: '))
        numeros.write(str(novo_numero) + '\n')
        aux += 1

    except ValueError:
        print('Digite apenas números inteiros!')

numeros.close()

numeros = open('C:\\WorkSpace\\' + nome_arquivo + '.txt', 'r')

for linhas in numeros:
    armazena_numeros.append(linhas)

for i in armazena_numeros:
    print(i)

numeros.close()
