from conexao import ConectaBanco
import time
import keyboard


conexao = ConectaBanco()


def tempo_inicial():
    return time.time()


def tempo_decorrido(tempo_inicial):
    decorrido = time.time() - tempo_inicial
    return round(decorrido, 1)


conexao.delete("""delete from automoveis where id <= 10000""")


def aplicacao(n):
    lista_id = []
    t_inicial = tempo_inicial()
    lista_tempo = []
    for i in range(0, n):
        conexao.insert(f"""insert into automoveis values ({i+1}, 'ferrari', 2020)""")
        lista_id.append(i+1)
        t_decorrido = tempo_decorrido(t_inicial)
        if t_decorrido % 1 == 0 and t_decorrido not in lista_tempo:
            lista_tempo.append(t_decorrido)
            print(f'Tempo decorrido: {t_decorrido}, Númedo de inserções: {i+1}, aperte c para cancelar')
        if keyboard.is_pressed('c'):
            for id in lista_id:
                conexao.delete(f"""delete from automoveis where id = {id}""")
            print('Dados deletados com sucesso!')
            return
    print('Dados inseridos com sucesso!')


def sgbd(n):
    mil = 1000
    n = n < mil and mil or n
    query = """ BEGIN TRAN """
    count_id = 0
    t_inicial = tempo_inicial()
    lista_tempo = []
    sucesso = True
    for i in range(int(n/mil)):
        query += """ BEGIN TRAN """
        query += """ insert into automoveis values """
        for y in range(0, mil):
            count_id += 1
            query += f""" ({count_id}, 'Ferrari', 2020) """
            if y+1 < 1000:
                query += """ , """
            else:
                query += """ COMMIT TRAN """
            t_decorrido = tempo_decorrido(t_inicial)
            if t_decorrido % 1 == 0 and t_decorrido not in lista_tempo:
                lista_tempo.append(t_decorrido)
                print(f'Tempo decorrido: {t_decorrido}, Númedo de inserções: {count_id}, aperte c para cancelar')
            if keyboard.is_pressed('c'):
                sucesso = False
        if not sucesso:
            query += """ COMMIT TRAN """
            break
    if sucesso:
        query += """ COMMIT TRAN """
    else:
        query += """ ROLLBACK TRAN """

    conexao.insert(query)
    print(sucesso and 'Transação realizada com sucesso!' or 'Transação cancelada')


while True:
    opcao = input('Digite 1 para fazer a transação na aplicação ou 2 para transação no SGBdD: ')
    if opcao == '1':
        aplicacao(10000)
        break

    elif opcao == '2':
        sgbd(100000)
        break


if __name__ == '__main__':
    pass
