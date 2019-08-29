'''27 - Duas amigas estabeleceram o código abaixo para que suas mensagens não fossem lidas pelas demais pessoas.
 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
' ' a b  c d e f  g h  i   j    k   l    m  n    o  p   q   r    s   t   u   v    w  x   y   z
Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0. Faça um método para "traduzir",
que recebe uma lista com uma mensagem (secreta) e "traduz" a sequência armazenada em uma lista.'''


def traducao():
    codigo = {0: ' ', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
                13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
    codigo_digitado = []

    print('Digite o código: ')
    while True:
        try:
            numero = int(input('Código: '))
            if numero >= 0 or numero <= 26:
                codigo_digitado.append(numero)
                opcao = input('Para digitar mais um código digite 1 ou qualquer outra tecla para sair: ')
                if opcao != '1':
                    break

            else:
                print('Digite apenas números de 0 a 26!')

        except ValueError:
            print('Digite apenas números de 0 a 26!')

    for i in range(len(codigo_digitado)):
        print(codigo[codigo_digitado[i]], end='')


if __name__ == '__main__':
    traducao()