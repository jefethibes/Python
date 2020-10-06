deslocamento = []  # lista que vai armazenar o deslocamento

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # lista do alfabeto


def criptografia(texto, chave):  # função que criptografa o texto
    cripto = ''  # variável que armazena o texto criptografado
    i = 0  # variável contadora

    for letra in texto:  # for que percorre o texto
        index_desloc = 0  # reseta variável que armazena o deslocamento
        if i >= len(chave):  # se i for maior que o tamanho da chave, reseta para começar a chave novamente
            i = 0  # reseta i
        if letra in alfabeto:  # se for uma letra do alfabeto entra aqui
            index_desloc = alfabeto.index(chave[i]) + alfabeto.index(letra)
            # pega o index do alfabeto correspondente a letra da chave + o index do alfabeto correspondente a letra
            deslocamento.append(index_desloc)  # adiciona o deslocamento na lista
            if index_desloc >= len(alfabeto):  # se o deslocamento for maior que 25 entra aqui
                index_desloc = index_desloc - len(alfabeto)  # dimiui o deslocamento pelo tamanho do alfabeto
                cripto += alfabeto[index_desloc]  # adiciona a letra do alfabeto correspondente ao deslocamento
                i += 1  # adiciona +1 a i
            else:  # se deslocamento for menor que 26 entra aqui
                cripto += alfabeto[index_desloc]  # adiciona a letra do alfabeto correspondente ao deslocamento
                i += 1  # adiciona +1 a i
        else:  # se não for uma letra entra aqui
            cripto += letra  # adiciona espaços, números e pontuações

    return cripto  # retorna a criptografia


def descriptografia(texto, chave):  # função que descriptografa o texto
    descripto = ''  # armazena a descriptograia
    i = 0  # contador
    y = 0  # contador

    for letra in texto:  # percorre a criptografia letra por letra
        if i >= len(chave):  # se i for maior que o tamanho da chave, reseta i
            i = 0  # reseta i
        if letra in alfabeto:  # se for uma letra do alfabeto entra aqui
            descripto += alfabeto[deslocamento[y] - alfabeto.index(chave[i])]
            # adiciona a letra correspondente ao index do deslocamento - index da letra da chave
            i += 1  # i recebe +1
            y += 1  # y recebe +1
        else:  # se for número, pontuação ou espaço continua igual
            descripto += letra  # adiciona o que não for letra

    return descripto  # retorna o texto descriptografado


texto = input('Digite o texto que será criptografado: ').lower()
# recebe o texto que sera criptografado em letras minusculas

chave = input('Digite a chave de criptografia(apenas letras): ')
# recebe a chave que será utilizada na criptografia

crip = criptografia(texto, chave)
# chama a função de criptografia e passa o texto e a chave

descripto = descriptografia(crip, chave)
# chama a função de descriptografia e passa a criptografia e a chave

print(crip) # printa a criptografia
print(descripto) # printa o texto descriptografado
