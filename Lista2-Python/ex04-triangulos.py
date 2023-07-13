# Exercício 2.4 - Triângulos

#importando a biblioteca math para resolução do exercício
import math

#enviando uma requisição ao cliente enviar o número das três variáveis do triângulo
variavelA = float(input()) 
variavelB = float(input())
variavelC = float(input())

#condição para entender em qual triângulo o trio de variáveis se encaixa 
if variavelA >= variavelB + variavelC:
  print('NAO FORMA TRIANGULO')
elif math.pow(variavelA,2) == math.pow(variavelB,2) + math.pow(variavelC,2):
  print('TRIANGULO RETANGULO')
elif math.pow(variavelA,2) > math.pow(variavelB,2) + math.pow(variavelC,2):
  print('TRIANGULO OBTUSANGULO')
elif math.pow(variavelA,2) < math.pow(variavelB,2) + math.pow(variavelC,2):
  print('TRIANGULO ACUTANGULO')
if variavelA == variavelB and variavelA == variavelC:
  print('TRIANGULO EQUILATERO')
if (variavelA == variavelB and variavelA != variavelC) or (variavelB == variavelC and variavelB != variavelA):
  print('TRIANGULO ISOSCELES')