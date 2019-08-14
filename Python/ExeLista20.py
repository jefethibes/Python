"""20 - Crie um classe Funcionário com os atributos nome, idade e salário. Deve ter  um método
aumenta_salario. Crie duas subclasses da classe funcionário, programador  e  analista, implementando
o método  nas duas subclasses. Para o programador some ao atributo salário mais 20 e ao analista some
ao salário mais 30,  mostrando na tela o valor. Depois disso, crie uma classe de testes instanciando
os objetos programador e analista e chame o método  aumenta_salario de cada um."""


class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def aumenta_salario(self, aumento):
        self.salario = self.salario + aumento
        print('O novo salário é R$ {:.2f}'.format(self.salario))


class Programador(Funcionario):
    def aumenta_salario(self, aumento):
        super().aumenta_salario(aumento=20)


class Analista(Funcionario):
    def aumenta_salario(self, aumento):
        super().aumenta_salario(aumento=30)


class Main:
    nome = input('Nome do programador: ')

    while True:
        try:
            idade = int(input('Idade: '))
            break

        except ValueError:
            print('Não é uma idade válida!')

    while True:
        try:
            salario = float(input('Salário: '))
            break

        except ValueError:
            print('Não é um salário válido!')

    programador = Programador(nome, idade, salario)
    programador.aumenta_salario(salario)

    nome = input('Nome do programador: ')

    while True:
        try:
            idade = int(input('Idade: '))
            break

        except ValueError:
            print('Não é uma idade válida!')

    while True:
        try:
            salario = float(input('Salário: '))
            break

        except ValueError:
            print('Não é um salário válido!')

    analista = Analista(nome, idade, salario)
    analista.aumenta_salario(salario)
    

if __name__ == '__main__':
    Main()