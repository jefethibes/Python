def cripitografar(cripto, cif):  # função de criptografia
    aux = ''  # variável que armazena a criptografia
    for char in cripto:  # percorre o texto letra por letra
        aux += chr(ord(char) + cif)  # pega o caracter na tabela ascii e soma com a sifra
    return aux  # retorna a criptografia


def descriptografar(cripto, cif):  # função que descriptografa
    aux = ''  # variavel que armazena o texto descriptografado
    for char in cripto:  # percorre a criptografia letra por letra
        aux += chr(ord(char) - cif)  # pega o caracte na tabela ascii e diminui a cifra
    return aux  # retorna o texto descriptografado


texto = input('Digite o texto: ')  # recebe o texto

cifra = int(input('Digite o número de casas para a criptografia: '))  # recebe a cifra

crip = cripitografar(texto, cifra)  # passa o texto e a cifra para criptografia

descrip = descriptografar(crip, cifra)  # passa a criptografia e a cifra para a descriptografia

print('Criptografia: {}'.format(crip))  # printa a criptografia
print('Descriptograia: {}'.format(descrip))  # printa a descriptografia
