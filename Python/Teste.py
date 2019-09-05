#1- Escreva uma classe que contém um método que calcule se a pessoa é maior de 18 anos ou não.
#   Receba os dados pela console e chame este método.

#   (modifique este exercício para receber 5 alunos, 3 notas para cada um e calcule a média mostrando se está aprovado ou não)


import unittest


class validacao():

    def valida_idade_maior_18(self, idade):
        if idade >= 18:
            return "Maior de idade"
        else:
            return "Menor de idade"


class ExecutaClasse:
    def execucao(self):
        valida = validacao()
        print(valida.valida_idade_maior_18(int(input("Digite idade: "))))


class validacaoTest(unittest.TestCase):
    def test_validacao(self):
        valida = validacao()
        resultado = valida.valida_idade_maior_18(19)
        self.assertEquals(resultado, "Maior de idade")


class validacaoTest2(unittest.TestCase):
    def test_validacao(self):
        valida = validacao()
        resultado = valida.valida_idade_maior_18(5)
        self.assertEquals(resultado, "Menor de idade")
