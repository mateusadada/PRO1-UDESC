import sys

from Contribuinte import Contribuinte

##################################################

# Questão 13: Qual o código necessário para criar o programa principal?
pessoa=Contribuinte()
pessoa.Leitura()
pessoa.Calcular()
print(pessoa.toString())
del(pessoa)

# Questão 14: Qual o comando que encerra o programa principal?
sys.exit(0)

##################################################
