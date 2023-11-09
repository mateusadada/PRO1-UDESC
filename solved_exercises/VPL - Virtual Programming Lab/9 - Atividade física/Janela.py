import sys
from tkinter import *

##################################################

class Janela( Questão 01 ): ## (Complete o código que declara a classe)
    __Lb_homem=None
    __Lb_mulher=None
    __Lb_ciclismo=None
    __Lb_corrida=None
    __Lb_natacao=None
    __Lb_total_calorias = None
    __Lb_diferenca = None
    __Et_homem_ciclismo=None
    __Et_homem_corrida=None
    __Et_homem_natacao=None
    __Et_mulher_ciclismo=None
    __Et_mulher_corrida=None
    __Et_mulher_natacao=None
    __Et_total_homem = None
    __Et_total_mulher = None
    __Et_diferenca = None
    __Bt_calc=None

    ## Questão 02:  (Criar o construtor da classe Janela)

    def action_total_homem(self):
        ## Questão 03:  (Criar o evento que calcula o consumo
        ##               total de calorias do homem)

    def action_total_mulher(self):
        ## Questão 04:  (Criar o evento que calcula o consumo
        ##               total de calorias da mulher)

    def action_diferenca(self):
        ## Questão 05:  (Criar o evento que calcula a diferença
        ##               de consumo de calorias entre o homem e a mulher)

    def action_exit(self):
        ## Questão 06:  (Qual o código necessário para encerrar
        ##               o programa no canto superior direito da janela?)

    def action_Bt_calc(self):
        ## Questão 07:  (Chamar os eventos que fazem os cálculos
        ##               citados em 03, 04, 05)

    def inicialize(self):
        ## Questão 08:  (Alocar os componentes gráficos)

        self.__Bt_calc=Button(self, text='Calcular', command= Questão 09 )
        ## Questão 09: (Qual o comando que associa o botão Bt_calc ao evento
        ##              que realiza os cálculos da Questão 07?)

        ############# Grid #############
        ## Questão 10:  (Acrescentar na tela os componentes gráficos)

        self.protocol("WM_DELETE_WINDOW", self.action_exit)
        
##################################################
