import sys
from Roupa import Roupa

# Questão 07: Qual o código necessário para criar o programa principal?
teste=Roupa()
teste.Leitura()
teste.Calcula_Total()
print(teste.toString())
del(teste)

# Questão 08: Qual o comando que encerra o programa principal?
sys.exit(0)
