'''Faça a tabuada de 1 até 10 e salve cada uma em um arquivo, depois leia e mostre na tela'''


for i in range(1, 11, 1):
    arquivo = open('C:\\WorkSpace\\' + str(i) + '.txt', 'w')
    for x in range(1, 11, 1):
        aux = i * x
        arquivo.write(str(i) + 'X' + str(x) + '=' + str(aux) + '\n')
    arquivo.write('-------------------------------------')
    arquivo.close()

for i in range(1, 11, 1):
    arquivo = open('C:\\WorkSpace\\' + str(i) + '.txt', 'r')
    for linha in arquivo:
        print(linha)
    arquivo.close()
