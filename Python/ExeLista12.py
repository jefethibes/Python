#12 - Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

while True:
    try:
        valor_um = float(input('Digite um número: '))
        break

    except ValueError:
        print('Digite apenas números!')

while True:
    try:
        valor_dois = float(input('Digite outro número: '))
        if valor_dois != valor_um:
            break

        else:
            print('Digite um número diferente do primeiro!')

    except ValueError:
        print('Digite apenas números!')

if valor_um > valor_dois:
    print('O maior número é {}'.format(valor_um))

else:
    print('O maior número é {}'.format(valor_dois))