import sys
from tkinter import *

##################################################


class Janela(Tk):  # Questão 01: (Complete o código que declara a classe)
    __Lb_valor1=None
    __Lb_valor2=None
    __Lb_result=None
    __Et_valor1=None
    __Et_valor2=None
    __Et_result=None
    __Bt_adic=None
    __Bt_sub=None
    __Bt_mult=None
    __Bt_div=None
    
    # Questão 02: (Criar o construtor da classe Janela)
    def __init__(self, string='Janela', px=100, py=100, dx=380, dy=140, cor='orange'):
        super().__init__()
        self.title(string)
        self.geometry("%dx%d+%d+%d" % (dx, dy, px, py))
        self.configure(bg=cor)

        self.inicialize()
    
    def action_exit(self):
        # Questão 03: (Qual o código necessário para encerrar o programa no canto
        #              superior direito da janela)
        print("Destruindo a Janela...")
        self.destroy()
        sys.exit(0)
    
    def action_Bt_adic(self):
        # Questão 04: (Criar o evento que calcula a adição dos valores numéricos)
        n1 = float(self.__Et_valor1.get())
        n2 = float(self.__Et_valor2.get())
        total = n1 + n2
        self.__Et_result.delete(0, END)
        self.__Et_result.insert(END, "%5.2f" % total)

    def action_Bt_sub(self):
        # Questão 05: (Criar o evento que calcula a subtração dos valores numéricos)
        n1 = float(self.__Et_valor1.get())
        n2 = float(self.__Et_valor2.get())
        total = n1 - n2
        self.__Et_result.delete(0, END)
        self.__Et_result.insert(END, "%5.2f" % total)

    def action_Bt_mult(self):
        # Questão 06: (Criar o evento que calcula a multiplicação dos valores numéricos)
        n1 = float(self.__Et_valor1.get())
        n2 = float(self.__Et_valor2.get())
        total = n1 * n2
        self.__Et_result.delete(0, END)
        self.__Et_result.insert(END, "%5.2f" % total)

    def action_Bt_div(self):
        # Questão 07: (Criar o evento que calcula a divisão dos valores numéricos)
        n1 = float(self.__Et_valor1.get())
        n2 = float(self.__Et_valor2.get())
        total = n1 / n2
        self.__Et_result.delete(0, END)
        self.__Et_result.insert(END, "%5.2f" % total)

    def inicialize(self):
        # Questão 08: (Realize a alocação dos componentes gráficos)
        self.__Lb_valor1 = Label(self, text="Valor1:", width=12)
        self.__Lb_valor2 = Label(self, text="Valor2:", width=12)
        self.__Lb_result = Label(self, text="Resultado:", width=12)

        self.__Lb_valor1.configure(bg='yellow', anchor=E)
        self.__Lb_valor2.configure(bg='yellow', anchor=E)
        self.__Lb_result.configure(bg='yellow', anchor=E)

        self.__Et_valor1 = Entry(self, width=28)
        self.__Et_valor2 = Entry(self, width=28)

        self.__Et_result = Entry(self, width=28)
        self.__Et_result.configure(bg='lightgray')

        self.__Bt_adic=Button(self, text='Adic', command=self.action_Bt_adic)
        # Questão 09: (Qual o comando que associa o botão Bt_Adic ao evento que realiza
        #              os cálculos da Questão 04?)
        
        self.__Bt_sub=Button(self, text='Sub', command=self.action_Bt_sub)
        # Questão 10: (Qual o comando que associa o botão Bt_Sub ao evento que realiza
        #              os cálculos da Questão 05?)
        
        self.__Bt_mult=Button(self, text='Mult', command=self.action_Bt_mult)
        # Questão 11: (Qual o comando que associa o botão Bt_Mult ao evento que realiza
        #              os cálculos da Questão 06?)
        
        self.__Bt_div=Button(self, text='Div', command=self.action_Bt_div)
        # Questão 12: (Qual o comando que associa o botão Bt_Div ao evento que realiza
        #              os cálculos da Questão 07?)
        
        ############# Grid #############
        # Questão 13: (Acrescentar os componentes gráficos na Tela)
        self.__Lb_valor1.grid(row=0, column=0, sticky=NW, padx=4, pady=4)
        self.__Lb_valor2.grid(row=1, column=0, sticky=NW, padx=4, pady=4)

        self.__Et_valor1.grid(row=0, column=1, columnspan=4, sticky=NW, padx=4, pady=4)
        self.__Et_valor2.grid(row=1, column=1, columnspan=4, sticky=NW, padx=4, pady=4)

        self.__Bt_adic.grid(row=2, column=1, sticky=NW, padx=4, pady=4)
        self.__Bt_sub.grid(row=2, column=2, sticky=NW, padx=4, pady=4)
        self.__Bt_mult.grid(row=2, column=3, sticky=NW, padx=4, pady=4)
        self.__Bt_div.grid(row=2, column=4, sticky=NW, padx=4, pady=4)

        self.__Lb_result.grid(row=3, column=0, sticky=NW, padx=4, pady=4)
        self.__Et_result.grid(row=3, column=1, columnspan=4, sticky=NW, padx=4, pady=4)

        self.protocol("WM_DELETE_WINDOW", self.action_exit)

##################################################
