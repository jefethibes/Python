"""1- Escreva uma classe que contém um método que calcule se a pessoa é maior de 18 anos ou não.
Receba os dados pela console e chame este método. (modifique este exercício para receber 5 alunos,
3 notas para cada um e calcule a média mostrando se está aprovado ou não)"""

class Aluno:
    def nome(self):
        nome_aluno = input('Nome do aluno: ')

    def media(self):
        while True:
            try:
                n1 = float(input('N1: '))
                if n1 <= 10 and n1 >= 0:
                    break

                else:
                    print('Digite a nota entre 0 e 10!')

            except ValueError:
                print('Digite a nota entre 0 e 10!')

        while True:
            try:
                n2 = float(input('N2: '))
                if n2 <= 10 and n2 >= 0:
                    break

                else:
                    print('Digite a nota entre 0 e 10!')

            except ValueError:
                print('Digite a nota entre 0 e 10!')

        while True:
            try:
                n3 = float(input('N3: '))
                if n3 <= 10 and n3 >= 0:
                    break

                else:
                    print('Digite a nota entre 0 e 10!')

            except ValueError:
                print('Digite a nota entre 0 e 10!')

        if (n1 + n2 + n3) / 3 > 6:
            print('Média {:.2f}! Aprovado!'.format((n1 + n2 + n3) / 3))

        else:
            print('Média {:.2f}! Reprovado!'.format((n1 + n2 + n3) / 3))

novo_aluno = Aluno()

for i in range(5):
    novo_aluno.nome()
    novo_aluno.media()