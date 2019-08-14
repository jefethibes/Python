"""18 - Crie uma classe animal com o método comer, este método deve
escrever na tela "o animal esta comendo". Depois disso crie as classes
cachorro, cavalo e gato e implemente o método comer de acordo com o que cada animal
come. Crie uma classe AnimalTeste e coloque os três animais dentro de uma lista de
animais e chame o método comer polimorficamente (com um for)"""


class Animal:
    def comer(self):
        print('O animal esta comendo',end=' ')


class Cachorro(Animal):
    def comer(self):
        super().comer()
        print('ração!')


class Cavalo(Animal):
    def comer(self):
        super().comer()
        print('milho!')


class Gato(Animal):
    def comer(self):
        super().comer()
        print('peixe!')


class AnimalsTeste(Animal):
    animais = [Cachorro(), Cavalo(), Gato()]

    for i in animais:
        i.comer()
