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

        self.form.grid(row=0, column=0)
        self.calc.grid(row=1, column=0)
        self.resultado.grid(row=2, column=0)

        self.anchor('n')


# programa principal
janela = Janela()
janela.mainloop()
