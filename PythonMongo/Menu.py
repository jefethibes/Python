from Imovel import Imoveis


class Menu:
    imovel = Imoveis()
    while True:
        print('----------------Imobiliária Tabajara----------------\n'
              '1 - Adicionar imóvel\n'
              '2 - Listar imóvel\n'
              '3 - Listar todos os imóveis\n'
              '4 - Alterar imóvel\n'
              '5 - Remover imóvel\n'
              '6 - Sair do sistema')
        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            imovel.novo_imovel()

        elif opcao == '2':
            imovel.listar_imovel()

        elif opcao == '3':
            imovel.listar_imoveis()

        elif opcao == '4':
            imovel.remover_imovel()
            imovel.novo_imovel()

        elif opcao == '5':
            imovel.remover_imovel()

        elif opcao == '6':
            exit()

        else:
            print('Opção inválida!')
