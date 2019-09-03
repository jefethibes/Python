'''32 - Lançar nota final para 3 alunos, deve ser possível adicionar, atualizar e deletar.
Apresente o resultado somente a nota de cada aluno ao final das operações.
33 - Incremente o exercício anterior para receber 3 notas para cada aluno,
onde deve ser possível efetuar as operações de adicionar, atualizar e deletar
e mostre a média. (se possível você pode aproveitar exercícios anteriores)'''


class Alunos:
    alunos = []

    def adicionar(self):
        aux = []

        nome = input('Nome do aluno: ')
        aux.append(nome)

        while len(aux) < 2:
            try:
                n1 = float(input('N1: '))
                if n1 <= 10 and n1 >= 0:
                    aux.append(n1)
                    break

                else:
                    print('Nota inválida!')

            except ValueError:
                print('Nota inválida!')

        while len(aux) < 3:
            try:
                n2 = float(input('N2: '))
                if n2 <= 10 and n2 >= 0:
                    aux.append(n2)
                    break

                else:
                    print('Nota inválida!')

            except ValueError:
                print('Nota inválida!')

        while len(aux) < 4:
            try:
                n3 = float(input('N3: '))
                if n3 <= 10 and n3 >= 0:
                    aux.append(n3)
                    break

                else:
                    print('Nota inválida!')

            except ValueError:
                print('Nota inválida!')

        self.alunos.append(aux[:])

    def atualiza(self):
        valida_nome = False
        if len(self.alunos) == 0:
            print('Não há alunos cadastrados!')

        else:
            nome = input('Digite o nome do aluno: ')
            for i in range(len(self.alunos)):
                if nome == self.alunos[i][0]:
                    valida_nome = True
                    del self.alunos[i]
                    self.adicionar()
                    break

            if valida_nome is False:
                print('Aluno não cadastrado!')

    def deletar(self):
        valida_nome = False
        if len(self.alunos) == 0:
            print('Não há alunos cadastrados!')

        else:
            nome = input('Digite o nome do aluno: ')
            for i in range(len(self.alunos)):
                if nome == self.alunos[i][0]:
                    valida_nome = True
                    del self.alunos[i]
                    print('Aluno removido com sucesso!')
                    break

            if valida_nome is False:
                print('Aluno não cadastrado!')

    def media(self):
        if len(self.alunos) == 0:
            print('Não há alunos cadastrados!')

        else:
            for i in range(len(self.alunos)):
                print('Aluno: {}'.format(self.alunos[i][0]))
                print('Notas: {:.2f}, {:.2f}, {:.2f}'.format(self.alunos[i][1], self.alunos[i][2], self.alunos[i][3]))
                print('Média: {:.2f}'.format((self.alunos[i][1] + self.alunos[i][2] + self.alunos[i][3]) / 3))
                print('-----------------------------')


def main():
    while True:
        novo_aluno = Alunos()

        print('Menu:\n'
              '1 - Adicionar aluno e notas\n'
              '2 - Atualizar notas\n'
              '3 - Deletar aluno e notas\n'
              '4 - Media\n'
              '5 - Sair')
        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            novo_aluno.adicionar()

        elif opcao == '2':
            novo_aluno.atualiza()

        elif opcao == '3':
            novo_aluno.deletar()

        elif opcao == '4':
            novo_aluno.media()

        elif opcao == '5':
            exit()

        else:
            print('Opção inválida!')


if __name__ == '__main__':
    main()
