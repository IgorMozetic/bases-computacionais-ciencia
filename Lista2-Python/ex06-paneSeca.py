# Exercício 2.6 - Pane seca?

#importando a biblioteca math para resolução do exercício
import math

#enviando uma requisição ao cliente enviar o número das quatro variáveis, da eficiência do carro e da quantidade de litros que o carro tem
variavelX1 = float(input()) 
variavelY1 = float(input())
variavelX2 = float(input())
variavelY2 = float(input())
eficienciaCarro = float(input())
qntLitrosCarro = float(input())

#calculos para descobrir a distância a ser percorrida e a distância que o carro consegue percorrer
distancia = math.sqrt(math.pow( (variavelX1 - variavelX2),2) + math.pow((variavelY1 - variavelY2),2) )
carroPercorre = eficienciaCarro * qntLitrosCarro

#condição para saber se o carro consegue percorrer a distância ou não
if distancia > carroPercorre:
  print('N')
else:
  print('S')