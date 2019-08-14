"""19 - Crie uma classe chamada Bicicleta. Ela terá os seguintes métodos: quantidadeMarchas();
tipoFreio() e marca(); Crie também duas classes que estendem esta classe, uma se chamará BicicletaPasseio
e a outra BicicletaProfissional. Para ﬁnalizar crie uma classe onde deverá estar o método main e crie uma
instancia de cada tipo de bicicleta e mostre o resultado dos métodos."""


class Bicicleta:
    def tipo_bicicleta(self):
        print('Bicicleta', end=' ')

    def quantidade_marchas(self):
        print('Marchas:', end=' ')

    def tipo_freio(self):
        print('Freio:', end=' ')

    def marca(self):
        print('Marca:', end=' ')


class BicicletaPasseio(Bicicleta):
    def tipo_bicicleta(self):
        super().tipo_bicicleta()
        print('passeio:')

    def quantidade_marchas(self):
        super().quantidade_marchas()
        print('18')

    def tipo_freio(self):
        super().tipo_freio()
        print('normal')

    def marca(self):
        super().marca()
        print('Bandeirantes')


class BicicletaProfissional(Bicicleta):
    def tipo_bicicleta(self):
        super().tipo_bicicleta()
        print('profissional:')

    def quantidade_marchas(self):
        super().quantidade_marchas()
        print('24')

    def tipo_freio(self):
        super().tipo_freio()
        print('abs')

    def marca(self):
        super().marca()
        print('Caloy')

class Main():
    bici_passeio = BicicletaPasseio()

    bici_passeio.tipo_bicicleta()
    bici_passeio.quantidade_marchas()
    bici_passeio.tipo_freio()
    bici_passeio.marca()

    bici_profissional = BicicletaProfissional()

    bici_profissional.tipo_bicicleta()
    bici_profissional.quantidade_marchas()
    bici_profissional.tipo_freio()
    bici_profissional.marca()


if __name__ == '__main__':
    Main()
