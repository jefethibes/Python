"""4 - Faça um programa que receba um valor que é o valor pago, um segundo valor que é o preço do produto e
retorne o troco a ser dado. (modifique para receber um valor de desconto e subtraia do valor do produto)"""

while True:
    try:
        valor_pago = float(input('Digite o valor pago: '))
        if valor_pago > 0:
            break

    except ValueError:
        print('Não é um valor válido!')

while True:
    try:
        valor_produto = float(input('Digite o valor do produto: '))
        if valor_produto > 0:
            break

    except ValueError:
        print('Não é um valor válido!')

while True:
    try:
        desconto = float(input('Digiter a % do desconto: '))
        if desconto >= 0 and desconto <= 100:
            break

    except ValueError:
        print('Não é um valor válido!')

valor_final = valor_produto - ((valor_produto / 100) * desconto)
troco = valor_pago - valor_final

if troco >= 0:
    print('Valor do produto: {:.2f}'.format(valor_produto))
    print('Desconto          {}%'.format(desconto))
    print('Valor Final:   R$ {:.2f}'.format(valor_final))
    print('Troco:         R$ {:.2f}'.format(troco))

else:
    print('Valor do produto: {:.2f}'.format(valor_produto))
    print('Desconto          {}%'.format(desconto))
    print('Valor Final:   R$ {:.2f}'.format(valor_final))
    print('Faltam:        R$ {:.2f}'.format(troco))
