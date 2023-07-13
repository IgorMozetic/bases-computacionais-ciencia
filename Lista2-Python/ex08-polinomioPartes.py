# Exercício 2.8 - Polinômio por partes

#importando a biblioteca math para resolução do exercício
import math

#enviando uma requisição ao cliente enviar o valor do número da variável
variavelX = float(input())

#condição para testar qual o calculo que será realizado baseado no valor da variável
if variavelX >= 2 and variavelX < 3:
  calculo = math.pow((variavelX - 1),2) + 1
  print('{:.4f}'.format(calculo))
elif variavelX >= 3 and variavelX <= 7:
  calculo = 1 - (math.pow((variavelX - 4),2)) - 2
  print('{:.4f}'.format(calculo))
elif variavelX < 2 or variavelX > 7:
  calculo = 2
  print('{:.4f}'.format(calculo))