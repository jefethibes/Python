'''Faça um programa que crie um arquivo contendo o nome de 5 pessoas, se o nome informado
for igual ao seu nome crie outro arquivo somente com o seu nome.'''


arquivo = open('C:\\WorkSpace\\nomes.txt', 'w')

arquivo.write('Patricia\n'
              'Antônio\n'
              'Valentina\n'
              'Jeferson\n'
              'Stefani')

arquivo.close()

arquivo = open('C:\\WorkSpace\\nomes.txt', 'r')

for linha in arquivo:
    if 'Jeferson' in linha:
        novo_arquivo = open('C:\\WorkSpace\\meunome.txt', 'w')
        novo_arquivo.write('Jeferson')
        novo_arquivo.close()
