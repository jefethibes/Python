from Produto import Produtos


class Menu:

    produto = Produtos()

    while True:
        print('Menu:\n'
              '1 - Cadastrar produto\n'
              '2 - Remover produto\n'
              '3 - Listar produtos\n'
              '4 - Listar produto\n'
              '5 - Alterar produto\n'
              '6 - Sair')
        opcao = input('Digite a opção: ')

        if opcao == '1':
            produto.novo_produto()

        elif opcao == '2':
            produto.deletar()

        elif opcao == '3':
            produto.listar_todos()

        elif opcao == '4':
            produto.listar()

        elif opcao == '5':
            produto.alterar()

        elif opcao == '6':
            exit()

        else:
            print('Opção inválida!')
