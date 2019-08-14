"""13 - Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as
idades dos homens serão sempre diferentes entre si, bem como as das mulheres).
Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova,
e o produto das idades do homem mais novo com a mulher mais velha."""

mulheres = []
homens = []

def idade_mulheres():
    print('Digite a idades das duas mulheres:')
    while True:
        try:
            idade_um = int(input('Digite a primeira idade: '))
            mulheres.append(idade_um)
            break

        except ValueError:
            print('Não é uma idade válida!')

    while True:
        try:
            idade_dois = int(input('Digite a segunda idade: '))
            if idade_dois != idade_um:
                mulheres.append(idade_dois)
                break

            else:
                print('A segunda idade tem que ser diferente da primeira!')

        except ValueError:
            print('Não é uma idade válida!')

def idade_homens():
    print('Digite a idades dos dois homens:')
    while True:
        try:
            idade_um = int(input('Digite a primeira idade: '))
            homens.append(idade_um)
            break

        except ValueError:
            print('Não é uma idade válida!')

    while True:
        try:
            idade_dois = int(input('Digite a segunda idade: '))
            if idade_dois != idade_um:
                homens.append(idade_dois)
                break

            else:
                print('A segunda idade tem que ser diferente da primeira!')

        except ValueError:
            print('Não é uma idade válida!')

def calculos():
    print('A soma da idade do homem mais velho com a mulher mais nova é {}'.format(max(homens) + min(mulheres)))
    print('O produto da idade do homem mais novo com a mulher mais velha é {}'.format(min(homens) * max(mulheres)))

idade_mulheres()
idade_homens()
calculos()