from Roupa import Roupa


##################################################

class Camisa(Roupa):  # Complete o código que define a classe Camisa
    # Questão 08: Qual o código que define as características da classe Camisa?
    __Cam_Tipo = None
    __Cam_Botoes = None
    __Cam_Bolsos = None
    __Cam_Gola = None

    # Questão 09: Qual o código que define o construtor que inicia a características da classe Camisa?
    #             (Os valores iniciais encontram-se no diagrama de classes)
    def __init__(self):
        super().__init__()
        self.__Cam_Tipo = ''
        self.__Cam_Botoes = 0
        self.__Cam_Bolsos = 0
        self.__Cam_Gola = True

    def Leitura(self):
        # Questão 10: Qual o código necessário para efetuar a leitura das características da classe Camisa?
        self.__Cam_Tipo = str(input('Digite o tipo da camisa: '))
        self.__Cam_Botoes = int(input('Botões: '))
        self.__Cam_Bolsos = int(input('Bolsos: '))
        self.__Cam_Gola = bool(input('True ou False: '))
        Roupa.Leitura(self)

    def toString(self):
        # Questão 11: Qual o código necessário para imprimir em uma string todas as características da classe Camisa?
        texto = '\nImpressão das Camisas'
        texto += f'\nTipo de camisa={self.__Cam_Tipo}'
        texto += f'\nQuantidade de botões={self.__Cam_Botoes}'
        texto += f'\nQuantidade de bolsos={self.__Cam_Bolsos}'
        texto += f'\nTem gola={self.__Cam_Gola}\n'
        texto += Roupa.toString(self)
        return texto

    # Questão 12: Qual o código que define o destrutor da classe Camisa?
    #             O destrutor deve escrever na tela:
    #             Passei no destrutor da classe Camisa...
    def __del__(self):
        Roupa.__del__(self)
        print('Passei no destrutor da classe Camisa...')

##################################################
