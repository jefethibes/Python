"""10 - receba três notas de um aluno e informe se ele passou ou reprovou."""

notas = []

while len(notas) < 3:
    try:
        nota = float(input('Nota {}: '.format(len(notas) + 1)))
        if nota >= 0 and nota <= 10:
            notas.append(nota)

        else:
            print('Digite apenas notas de 0 a 10!')

    except ValueError:
        print('Digite apenas números!')

if sum(notas) / len(notas) >= 6:
    print('Média: {:.2f}, Aprovado!'.format(sum(notas) / len(notas)))

else:
    print('Média: {:.2f}, Reprovado!'.format(sum(notas) / len(notas)))