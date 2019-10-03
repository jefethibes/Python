from Conexao import ConectaMongo


class Imovel:

    def salvar_imovel(self, codigo, endereco, numero, valor):
        conexao = ConectaMongo()
        imovel = {'codigo': codigo, 'endereco': endereco, 'numero': numero, 'valor': valor}
        print(imovel)
        conexao.salvar(imovel)

    def listar_imovel(self, codigo):
        conexao = ConectaMongo()
        conexao.listar_codigo({'codigo': codigo})

    def listar_imoveis(self):
        conexao = ConectaMongo()
        conexao.listar_todos()

    def deletar_imovel(self, codigo):
        conexao = ConectaMongo()
        conexao.remover({'codigo': codigo})
        print('Imovel removido com sucesso!')

    def alterar_imovel(self, codigo, novo_imovel):
        conexao = ConectaMongo()
        conexao.alterar(codigo, novo_imovel)

