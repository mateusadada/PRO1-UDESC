import sys
from tkinter import *


##################################################


class Janela(Tk):  # (Complete o código que declara a classe)
    __Lb_homem = None
    __Lb_mulher = None
    __Lb_ciclismo = None
    __Lb_corrida = None
    __Lb_natacao = None
    __Lb_total_calorias = None
    __Lb_diferenca = None
    __Et_homem_ciclismo = None
    __Et_homem_corrida = None
    __Et_homem_natacao = None
    __Et_mulher_ciclismo = None
    __Et_mulher_corrida = None
    __Et_mulher_natacao = None
    __Et_total_homem = None
    __Et_total_mulher = None
    __Et_diferenca = None
    __Bt_calc = None

    # Questão 02: (Criar o construtor da classe Janela)
    def __init__(self, string='Janela', px=100, py=100, dx=720, dy=300, cor='orange'):
        super().__init__()
        self.title(string)
        self.geometry("%dx%d+%d+%d" % (dx, dy, px, py))
        self.configure(bg=cor)
        self.inicialize()

    def action_total_homem(self):
        # Questão 03: (Criar o evento que calcula o consumo
        #               total de calorias do homem)
        n1 = float(self.__Et_homem_ciclismo.get())
        n2 = float(self.__Et_homem_corrida.get())
        n3 = float(self.__Et_homem_natacao.get())
        total = n1 + n2 + n3
        self.__Et_total_homem.delete(0, END)
        self.__Et_total_homem.insert(END, " %6.2f" % total)

    def action_total_mulher(self):
        # Questão 04: (Criar o evento que calcula o consumo
        #               total de calorias da mulher)
        n1 = float(self.__Et_mulher_ciclismo.get())
        n2 = float(self.__Et_mulher_corrida.get())
        n3 = float(self.__Et_mulher_natacao.get())
        total = n1 + n2 + n3
        self.__Et_total_mulher.delete(0, END)
        self.__Et_total_mulher.insert(END, " %6.2f" % total)

    def action_diferenca(self):
        # Questão 05: (Criar o evento que calcula a diferença
        #               de consumo de calorias entre o homem e a mulher)
        n1 = float(self.__Et_total_homem.get())
        n2 = float(self.__Et_total_mulher.get())
        total = n1 - n2
        self.__Et_diferenca.delete(0, END)
        self.__Et_diferenca.insert(END, " %6.2f" % total)

    def action_exit(self):
        # Questão 06: (Qual o código necessário para encerrar
        #               o programa no canto superior direito da janela?)
        print("Destruindo a Janela...")
        self.destroy()
        sys.exit(0)

    def action_Bt_calc(self):
        # Questão 07: (Chamar os eventos que fazem os cálculos
        #               citados em 03, 04, 05)
        self.action_total_homem()
        self.action_total_mulher()
        self.action_diferenca()

    def inicialize(self):
        pass
        # Questão 08: (Alocar os componentes gráficos)
        self.__Lb_homem = Label(self, text="Homem", width=21, bg="yellow")
        self.__Lb_mulher = Label(self, text="Mulher", width=21, bg="yellow")
        self.__Lb_ciclismo = Label(self, text="Ciclismo:", width=21, bg="yellow")
        self.__Lb_corrida = Label(self, text="Corrida:", width=12, bg="yellow")
        self.__Lb_natacao = Label(self, text="Natação:", width=12, bg="yellow")
        self.__Lb_total_calorias = Label(self, text="Total calorias:", width=12, bg="yellow")
        self.__Lb_diferenca = Label(self, text="Diferença:", width=12, bg="yellow")

        self.__Et_homem_ciclismo = Entry(self, width=25)
        self.__Et_homem_corrida = Entry(self, width=25)
        self.__Et_homem_natacao = Entry(self, width=25)
        self.__Et_mulher_ciclismo = Entry(self, width=25)
        self.__Et_mulher_corrida = Entry(self, width=25)
        self.__Et_mulher_natacao = Entry(self, width=25)
        self.__Et_mulher_natacao = Entry(self, width=25)
        self.__Et_mulher_natacao = Entry(self, width=25)
        self.__Et_total_homem = Entry(self, width=25, bg="lightgrey")
        self.__Et_total_mulher = Entry(self, width=25, bg="lightgrey")
        self.__Et_diferenca = Entry(self, width=25, bg="lightgrey")

        # Questão 09: (Qual o comando que associa o botão Bt_calc ao evento
        #              que realiza os cálculos da Questão 07?)
        self.__Bt_calc = Button(self, text='Calcular', command=self.action_Bt_calc)

        ############# Grid #############
        # Questão 10: (Acrescentar na tela os componentes gráficos)
        self.__Lb_homem.grid(row=0, column=1, padx=4, pady=4, sticky=NW)
        self.__Lb_mulher.grid(row=0, column=2, padx=4, pady=4, sticky=NW)
        self.__Lb_ciclismo.grid(row=1, column=0, padx=4, pady=4, sticky=NW)
        self.__Lb_corrida.grid(row=2, column=0, padx=4, pady=4)
        self.__Lb_natacao.grid(row=3, column=0, padx=4, pady=4)
        self.__Lb_total_calorias.grid(row=5, column=0, padx=4, pady=4)
        self.__Lb_diferenca.grid(row=6, column=0, padx=4, pady=4)

        self.__Et_homem_ciclismo.grid(row=1, column=1, padx=4, pady=4)
        self.__Et_homem_corrida.grid(row=2, column=1, padx=4, pady=4)
        self.__Et_homem_natacao.grid(row=3, column=1, padx=4, pady=4)
        self.__Et_mulher_ciclismo.grid(row=1, column=2, padx=4, pady=4)
        self.__Et_mulher_corrida.grid(row=2, column=2, padx=4, pady=4)
        self.__Et_mulher_natacao.grid(row=3, column=2, padx=4, pady=4)
        self.__Et_total_homem.grid(row=5, column=1, padx=4, pady=4)
        self.__Et_total_mulher.grid(row=5, column=2, padx=4, pady=4)
        self.__Et_diferenca.grid(row=6, column=1, padx=4, pady=4)

        self.__Bt_calc.grid(row=4, column=1, sticky=NW, padx=4, pady=4)

        self.protocol("WM_DELETE_WINDOW", self.action_exit)

##################################################
