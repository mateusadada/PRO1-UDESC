import sys
from tkinter import *

##################################################

class Janela():  # Questão 01: (Complete o código que declara a classe)
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
    
    def action_Total_Flamengo(self):
        pass
        # Questão 03: (Criar o evento que calcula o total de torcedores do Flamengo)
    
    def action_Total_Vasco(self):
        pass
        # Questão 04: (Criar o evento que calcula o total de torcedores do Vasco)
    
    def action_exit(self):
        pass
        # Questão 05: (Qual o código necessário para encerrar o programa no canto superior direito da janela)
    
    def action_Bt_calc(self):
        pass
        # Questão 06: (Chamar os eventos que fazem os cálculos citados em 03, 04)
    
    def inicialize(self):
        pass
        # Questão 07: Realize a alocação dos componentes gráficos)
        
        self.__Bt_calc=Button(self, text='Calcular', command= Questão 08 )
        # Questão 08: (Qual o comando que associa o botão Bt_calc ao evento
        #              que realiza os cálculos da Questão 06 ?)
        
        ############# Grid #############
        # Questão 09: (Acrescentar os componentes gráficos na Tela)
        
        self.protocol("WM_DELETE_WINDOW", self.action_exit)

##################################################
