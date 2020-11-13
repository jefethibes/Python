from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Contador(App):

    def build(self):
        box = BoxLayout(orientation='vertical') #instancia do box layout e orientaos na posição vertical
        button = Button(text='Clique aqui :)', font_size=30, on_release=self.incrementar) #cria um botao, personaliza o texto e o tamanho da letra e chama o metodo incrementar toda vez que alguem clicar
        self.label = Label(text='1', font_size=30) #cria um campo de texto com tamanho da fonte personalizado
        box.add_widget(button) #adiciona o botao ao layout
        box.add_widget(self.label) #adiciona o campo de texto ao layout
        return box #retorna o layout

    def incrementar(self): #passa a variavel botao como argumento
        self.label.text = str(int(self.label.text) + 1) #toda vez que o botao e clicado ele soma +1 no campo de texto


if __name__ == '__main__':
    Contador().run()
