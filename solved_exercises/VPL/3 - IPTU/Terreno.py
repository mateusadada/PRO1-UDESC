class Terreno:
    # Questão 01: Qual o código que define as características da classe base terreno?
    __Endereco = None
    __Comprimento = None
    __Largura = None
    __AreaConstr = None
    __AreaTotal = None

    # Questão 02: Qual o código que define o construtor que inicia as características da classe terreno?
    #              (Os valores iniciais encontram-se no diagrama de classes)
    def __init__(self):
        self.__Endereco = ''
        self.__Comprimento = 0.0
        self.__Largura = 0.0
        self.__AreaConstr = 0.0
        self.__AreaTotal = 0.0

    def Leitura(self):
        # Questão 03: Qual o código necessário para efetuar a leitura das características da classe terreno?
        self.__Endereco = str(input('Digite o endereço: '))
        self.__Comprimento = float(input('Comprimento: '))
        self.__Largura = float(input('Largura: '))
        self.__AreaConstr = float(input('Área construída: '))

    def Calcular(self):
        # Questão 04: Qual o código necessário para calcular a área total do terreno?
        self.__AreaTotal = self.__Comprimento * self.__Largura

    def toString(self):
        # Questão 05: Qual o código necessário para imprimir em uma string todas as características da classe terreno?
        texto = f'Endereço: {self.__Endereco}'
        texto += f'\nComprimento: %5.2f' % self.__Comprimento
        texto += f'\nLargura: %5.2f' % self.__Largura
        texto += f'\nÁrea Construída: %5.2f' % self.__AreaConstr
        texto += f'\nÁrea Total: %5.2f\n' % self.__AreaTotal
        return texto

    # Questão 06: Qual o código que define o destrutor da classe Terreno? O destrutor deve escrever na tela:
    #              Passei no destrutor da classe Terreno...
    def __del__(self):
        print('Passei no destrutor da classe Terreno...')
