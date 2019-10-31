import psycopg2


class ConectaSQL:

    def __init__(self):
        try:
            self.conexao = psycopg2.connect(user='postgres',
                                                password='ads',
                                                host='127.0.0.1',
                                                port='5432',
                                                database='alunos')
            self.conexao.autocommit = True
            self.cursor = self.conexao.cursor()

        except Exception as e:
            print('Falha ao conectar!')
            print(e)

    def cadastrar(self, json):
        matricula = json['matricula']
        nome = json['nome']
        turma = json['turma']

        try:
            self.cursor.execute("Insert into alunos (matricula, nome, turma) values ({}, '{}', '{}');"
                                 .format(matricula, nome, turma))
            return 'Cadastro efetuado!'
        except Exception as e:
            print('Falha ao cadastrar!')
            print(e)

    def listar_todos(self):
        try:
            aux = self.cursor.execute('select * from alunos')
            aux = self.cursor.fetchall()

            return aux
        except Exception as e:
            print('Erro ao listar!')
            print(e)

    def consulta(self, matricula):
        try:
            aux = self.cursor.execute('select * from alunos where matricula = {}'.format(matricula))
            aux = self.cursor.fetchall()

            return aux
        except Exception as e:
            print('Erro ao listar!')
            print(e)

    def deletar(self, matricula):
        try:
            self.cursor.execute("Delete from alunos where matricula = {}".format(matricula))

            return 'Aluno removido com sucesso!'
        except Exception as e:
            print('Erro ao deletar!')
            print(e)

    def alterar(self, id, json):
        matricula = id
        nome = json['nome']
        turma = json['turma']

        try:
            self.cursor.execute("update alunos set nome= '{}', turma= '{}' where matricula= {};".format(nome, turma, matricula))

            return 'Aluno alterado com sucesso!'
        except Exception as e:
            print('Erro ao alterar!')
            print(e)
