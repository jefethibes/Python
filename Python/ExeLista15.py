#15 - Ler 10 valores (considere que não serão lidos valores iguais) e escrever o maior deles.

valores = []

while len(valores) < 10:
    try:
        valores.append(float(input('Digite um valos: ')))

    except ValueError:
        print('Digite apenas números!')

print('O maior valor é {}'.format(max(valores)))