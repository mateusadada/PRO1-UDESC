import sys
from Camisa import Camisa

# Questão 13: Qual o código necessário para criar o programa principal?
adidas=Camisa()
adidas.Leitura()
adidas.Calcula_Total()
print(adidas.toString())
del(adidas)

# Questão 14: Qual o comando que encerra o programa principal?
sys.exit(0)
