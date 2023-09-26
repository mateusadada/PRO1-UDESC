from tkinter import *

##################################################

class Janela():  # Questão 01: (Complete o código que declara a classe)
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
    
    def action_exit(self):
        pass
        # Questão 03: (Qual o código necessário para encerrar o programa no canto
        #              superior direito da janela)
    
    def action_Bt_adic(self):
        pass
        # Questão 04: (Criar o evento que calcula a adição dos valores numéricos)
    
    def action_Bt_sub(self):
        pass
        # Questão 05: (Criar o evento que calcula a subtração dos valores numéricos)
    
    def action_Bt_mult(self):
        pass
        # Questão 06: (Criar o evento que calcula a multiplicação dos valores numéricos)
    
    def action_Bt_div(self):
        pass
        # Questão 07: (Criar o evento que calcula a divisão dos valores numéricos)
    
    def inicialize(self):
        # Questão 08: (Realize a alocação dos componentes gráficos)
        
        self.__Bt_adic=Button(self, text='Adic', command= Questão 09 )
        # Questão 09: (Qual o comando que associa o botão Bt_Adic ao evento que realiza
        #              os cálculos da Questão 04?)
        
        self.__Bt_sub=Button(self, text='Sub', command= Questão 10 )
        # Questão 10: (Qual o comando que associa o botão Bt_Sub ao evento que realiza
        #              os cálculos da Questão 05?)
        
        self.__Bt_mult=Button(self, text='Mult', command= Questão 11 )
        # Questão 11: (Qual o comando que associa o botão Bt_Mult ao evento que realiza
        #              os cálculos da Questão 06?)
        
        self.__Bt_div=Button(self, text='Div', command= Questão 12 )
        # Questão 12: (Qual o comando que associa o botão Bt_Div ao evento que realiza
        #              os cálculos da Questão 07?)
        
        ############# Grid #############
        # Questão 13: (Acrescentar os componentes gráficos na Tela)
        
        self.protocol("WM_DELETE_WINDOW", self.action_exit)

##################################################
