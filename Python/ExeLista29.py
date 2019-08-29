#29 - Crie um dict com 5 nomes e idades, crie um segundo dict duplicando os itens.


nome_idade = {'Juliana': 18, 'Eduardo': 25, 'Luiz': 37, 'Aline': 32, 'Ana Julia': 15}
nome_idade2 = {}

nome_idade2.update(nome_idade)

print(nome_idade, nome_idade2)
