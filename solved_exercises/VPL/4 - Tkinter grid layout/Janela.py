from tkinter import *


##################################################

class Janela(Tk):  # Questão 01: (Complete o código que declara a classe)
    __Lb_nome = None
    __Lb_telefone = None
    __Lb_email = None
    __Lb_endereco = None
    __Et_nome = None
    __Et_telefone = None
    __Et_email = None
    __Et_endereco = None

    # Questão 02: (Criar o construtor da classe Janela)
    def __init__(self, string='Janela', px=200, py=200, dx=400, dy=100, cor='orange'):
        super().__init__()
        self.title(string)
        self.geometry('%dx%d+%d+%d' % (dx, dy, px, py))
        self.configure(background=cor)
        self.inicialize()

    def inicialize(self):
        # Questão 03: (Realize a alocação dos componentes gráficos)
        self.__Lb_nome = Label(self, text='Nome:', bg='yellow', width=15, anchor='e')
        self.__Lb_telefone = Label(self, text='Telefone:', bg='yellow', width=15, anchor='e')
        self.__Lb_email = Label(self, text='Email:',  bg='yellow', width=15, anchor='e')
        self.__Lb_endereco = Label(self, text='Endereço:',  bg='yellow', width=15, anchor='e')
        self.__Et_nome = Entry(self, width=45)
        self.__Et_telefone = Entry(self, width=45)
        self.__Et_email = Entry(self, width=45)
        self.__Et_endereco = Entry(self, width=45)

        # Questão 04: (Acrescentar os componentes gráficos na Tela)
        self.__Lb_nome.grid(row=0, column=0, padx=2, pady=2)
        self.__Lb_telefone.grid(row=1, column=0, padx=2, pady=2)
        self.__Lb_email.grid(row=2, column=0, padx=2, pady=2)
        self.__Lb_endereco.grid(row=3, column=0, padx=2, pady=2)
        self.__Et_nome.grid(row=0, column=1, padx=2, pady=2)
        self.__Et_telefone.grid(row=1, column=1, padx=2, pady=2)
        self.__Et_email.grid(row=2, column=1, padx=2, pady=2)
        self.__Et_endereco.grid(row=3, column=1, padx=2, pady=2)

##################################################
