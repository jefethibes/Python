arquivo = open('C:\\WorkSpace\TesteArquivo.txt', 'w')

arquivo.write('Teste de arquivos em Python\n')
arquivo.write('bla bla bla')

arquivo.close()

arquivo = open('C:\\WorkSpace\TesteArquivo.txt', 'r')

for linha in arquivo:
    print(linha)

arquivo.close()
