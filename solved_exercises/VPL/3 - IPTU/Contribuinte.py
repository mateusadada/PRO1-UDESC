from Terreno import Terreno

class Contribuinte(Terreno):  # Complete o código que define a classe Contribuinte
    # Questão 08: Qual o código que define as características da classe Contribuinte?
    __Nome = None
    __Endereco = None
    __Idade = None

    # Questão 09: Qual o código que define o construtor que inicia a características da classe Contribuinte?
    #              (Os valores iniciais encontram-se no diagrama de classes)
    def __init__(self):
        super().__init__()
        self.__Nome = ''
        self.__Endereco = ''
        self.__Idade = 0

    def Leitura(self):
        pass
        # Questão 10: Qual o código necessário para efetuar a leitura das características da classe Contribuinte?
        self.__Nome = str(input('Nome: '))
        self.__Endereco = str(input('Endereço: '))
        self.__Idade = int(input('Idade: '))
        Terreno.Leitura(self)

    def toString(self):
        # Questão 11: Qual o código necessário para imprimir em uma string todas
        #              as características da classe Contribuinte?
        texto = f'Nome: {self.__Nome}'
        texto += f'\nEndereço: {self.__Endereco}'
        texto += f'\nidade: {self.__Idade}\n'
        texto += Terreno.toString(self)
        return texto

    # Questão 12: Qual o código que define o destrutor da classe Contribuinte? O destrutor deve escrever na tela:
    #              Passei no destrutor da classe Contribuinte...
    def __del__(self):
        Terreno.__del__(self)
        print('Passei no destrutor da classe Contribuinte...')
