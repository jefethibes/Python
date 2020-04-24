import pyodbc
import time


class ConectaBanco:

    def __init__(self):
        try:
            self.conect = pyodbc.connect('Driver={SQL Server};'
                                         'Server=WIN8\SQLEXPRESS;'
                                         'Database=Animais;'
                                         'Trusted_Connection=yes;')
            self.cursor = self.conect.cursor()

            for i in range(250000):
                self.cursor.execute("INSERT INTO Animais([IDAnimal], [Tipo]) VALUES ('{}', 'Cachorro')".format(i))

            self.conect.commit()

            '''self.cursor.execute('SELECT [IDAnimal], [Tipo] FROM Animais')'''
            '''self.cursor.execute('SELECT * FROM Animais')
            for i in self.cursor:
                print(i)'''

            print('Dados inseridos com sucesso!')

            print(time.process_time())
        except Exception as e:
            print('Falha ao conectar!')
            print(e)


if __name__ == '__main__':
    ConectaBanco()
