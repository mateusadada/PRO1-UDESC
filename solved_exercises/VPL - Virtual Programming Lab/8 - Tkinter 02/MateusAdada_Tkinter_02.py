from tkinter import *


class Janela(Tk):
    form = None
    calc = None
    resultado = None

    def __init__(self):
        super().__init__()
        self.title('Calculadora para Estatística')
        self.geometry('800x600')
        self.inicialize()

    def inicialize(self):
        self.form = Entry(self)
        self.calc = Button(self, text='Calcule')
        self.resultado = Label(self, text='Resultado', fg='blue')

        # self.form.pack()
        # self.calc.pack()
        # self.resultado.pack()


# programa principal
janela = Janela()
janela.mainloop()
