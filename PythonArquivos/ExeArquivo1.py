'''Crie um arquivo chamado nomes.txt que permita que o usuário faça a inserção
de 10 nomes. Procure no arquivo o arquivo o nome ‘gisele’'''


arquivo = open('C:\\WorkSpace\\nomes.txt', 'w')

for nomes in range(3):
    nome = input('Digite um nome: ')
    arquivo.write(nome + '\n')

arquivo.close()

arquivo = open('C:\\WorkSpace\\nomes.txt', 'r')

for nomes in arquivo:
    if 'gisele' in nomes:
        print('O nome Gisele está armazenado no arquivo!')

arquivo.close()
