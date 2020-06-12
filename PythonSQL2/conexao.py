import pyodbc


class ConectaBanco:

    def __init__(self):
        try:
            self.conect = pyodbc.connect('Driver={SQL Server};'
                                         'Server=WIN8\SQLEXPRESS;'
                                         'Database=carros;'
                                         'Trusted_Connection=yes;')
            self.cursor = self.conect.cursor()
        except Exception as e:
            print('Falha ao conectar!')
            print(e)

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.conect.commit()
        except Exception as e:
            print(e)

    def delete(self, query):
        try:
            self.cursor.execute(query)
            self.conect.commit()
        except Exception as e:
            print(e)
