##################################################

class Roupa(object):
    ## Questão 01: Qual o código que define as características da classe base Roupa?
    __Roupa_Marca = None
    __Roupa_Cor = None
    __Roupa_Tam = None
    __Roupa_Quant = None
    __Roupa_Preco = None
    __Total_Roupa = None

    ## Questão 02: Qual o código que define o construtor que inicia as características da classe Roupa?
    ##             (Os valores iniciais encontram-se no diagrama de classes)
    def __init__(self):
        self.__Roupa_Marca = ''
        self.__Roupa_Cor = ''
        self.__Roupa_Tam = 0
        self.__Roupa_Quant = 0
        self.__Roupa_Preco = 0.0
        self.__Total_Roupa = 0.0

    def Leitura(self):
        pass
        ## Questão 03: Qual o código necessário para efetuar a leitura das características da classe Roupa?

    def Calcula_Total(self):
        pass
        ## Questão 04: Qual o código necessário para calcular a despesa total da compra das peças de roupa?

    def toString(self):
        pass
        ## Questão 05: Qual o código necessário para imprimir em uma string todas as características da classe Roupa?
    
    ## Questão 06: Qual o código que define o destrutor da classe Roupa?
    ##             O destrutor deve escrever na tela:
    ##             Passei no destrutor da classe Roupa...

##################################################
