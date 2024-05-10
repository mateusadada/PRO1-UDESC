import sys
from tkinter import *

class Janela(Tk):  # Questão 01: (Complete o código que declara a classe)
    __Lb_flamengo=None
    __Lb_vasco=None
    __Lb_torcida_total=None
    __Lb_pr=None
    __Lb_sc=None
    __Lb_rs=None
    __Et_flamengo_pr=None
    __Et_flamengo_sc=None
    __Et_flamengo_rs=None
    __Et_vasco_pr=None
    __Et_vasco_sc=None
    __Et_vasco_rs=None
    __Et_total_flamengo=None
    __Et_total_vasco=None
    __Bt_calc=None
    
    # Questão 02: (Criar o construtor da classe Janela)
    def __init__(self, string='Janela', px=100, py=100, dx=470, dy=200, cor='orange'):
        super().__init__()
        self.title(string)
        self.geometry("%dx%d+%d+%d" % (dx, dy, px, py))
        self.configure(bg=cor)

        self.inicialize()
    
    def action_Total_Flamengo(self):
        # Questão 03: (Criar o evento que calcula o total de torcedores do Flamengo)
        n1 = float(self.__Et_flamengo_pr.get())
        n2 = float(self.__Et_flamengo_sc.get())
        n3 = float(self.__Et_flamengo_rs.get())
        total = n1 + n2 + n3
        self.__Et_total_flamengo.delete(0, END)
        self.__Et_total_flamengo.insert(END, "%3.1f" % total)
    
    def action_Total_Vasco(self):
        # Questão 04: (Criar o evento que calcula o total de torcedores do Vasco)
        n1 = float(self.__Et_vasco_pr.get())
        n2 = float(self.__Et_vasco_sc.get())
        n3 = float(self.__Et_vasco_rs.get())
        total = n1 + n2 + n3
        self.__Et_total_vasco.delete(0, END)
        self.__Et_total_vasco.insert(END, "%3.1f" % total)
    
    def action_exit(self):
        # Questão 05: (Qual o código necessário para encerrar o programa no canto superior direito da janela)
        print("Destruindo a Janela...")
        self.destroy()
        sys.exit(0)
    
    def action_Bt_calc(self):
        # Questão 06: (Chamar os eventos que fazem os cálculos citados em 03, 04)
        self.action_Total_Flamengo()
        self.action_Total_Vasco()
    
    def inicialize(self):
        # Questão 07: Realize a alocação dos componentes gráficos)
        self.__Lb_flamengo = Label(self, text="Flamengo", width=21)
        self.__Lb_vasco = Label(self, text="Vasco", width=21)
        self.__Lb_pr = Label(self, text="Paraná", width=12)
        self.__Lb_sc = Label(self, text="Santa Catarina", width=12)
        self.__Lb_rs = Label(self, text="Rio G. do Sul", width=12)
        self.__Lb_torcida_total = Label(self, text="Torcida total:", width=12)

        self.__Lb_flamengo.configure(bg='yellow')
        self.__Lb_vasco.configure(bg='yellow')
        self.__Lb_pr.configure(bg='yellow')
        self.__Lb_sc.configure(bg='yellow')
        self.__Lb_rs.configure(bg='yellow')
        self.__Lb_torcida_total.configure(bg='yellow')

        self.__Et_flamengo_pr = Entry(self, width=25)
        self.__Et_vasco_pr = Entry(self, width=25)
        self.__Et_flamengo_sc = Entry(self, width=25)
        self.__Et_vasco_sc = Entry(self, width=25)
        self.__Et_flamengo_rs = Entry(self, width=25)
        self.__Et_vasco_rs = Entry(self, width=25)
        self.__Et_total_flamengo = Entry(self, width=25)
        self.__Et_total_vasco = Entry(self, width=25)

        self.__Et_total_flamengo.configure(bg='lightgray')
        self.__Et_total_vasco.configure(bg='lightgray')

        # Questão 08: (Qual o comando que associa o botão Bt_calc ao evento
        #              que realiza os cálculos da Questão 06?)
        self.__Bt_calc=Button(self, text='Calcular', command=self.action_Bt_calc)
        
        # Questão 09: (Acrescentar os componentes gráficos na Tela)
        self.__Lb_flamengo.grid(row=0, column=1, padx=4, pady=4, sticky=NW)
        self.__Lb_vasco.grid(row=0, column=2, padx=4, pady=4, sticky=NW)
        self.__Lb_pr.grid(row=1, column=0, padx=4, pady=4)
        self.__Lb_sc.grid(row=2, column=0, padx=4, pady=4)
        self.__Lb_rs.grid(row=3, column=0, padx=4, pady=4)
        self.__Lb_torcida_total.grid(row=5, column=0, padx=4, pady=4, sticky=NW)

        self.__Et_flamengo_pr.grid(row=1, column=1, padx=4, pady=4)
        self.__Et_vasco_pr.grid(row=1, column=2, sticky=NW, padx=4, pady=4)
        self.__Et_flamengo_sc.grid(row=2, column=1, sticky=NW, padx=4, pady=4)
        self.__Et_vasco_sc.grid(row=2, column=2, sticky=NW, padx=4, pady=4)
        self.__Et_flamengo_rs.grid(row=3, column=1, sticky=NW, padx=4, pady=4)
        self.__Et_vasco_rs.grid(row=3, column=2, sticky=NW, padx=4, pady=4)
        self.__Et_total_flamengo.grid(row=5, column=1, sticky=NW, padx=4, pady=4)
        self.__Et_total_vasco.grid(row=5, column=2, sticky=NW, padx=4, pady=4)

        self.__Bt_calc.grid(row=4, column=1, sticky=NW, padx=4, pady=4)

        self.protocol("WM_DELETE_WINDOW", self.action_exit)
