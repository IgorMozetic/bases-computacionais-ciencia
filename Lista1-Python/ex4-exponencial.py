# Exercício 1.4 - Exponencial Raiz e Fração

#importando a biblioteca math para utilização de suas funções
import math

#enviando uma requisição ao cliente enviar os número das variáveis
num1 = int(input())
num2 = int(input())
num3 = float(input()) 
num4 = float(input()) 

#realizando o calculo para achar o resultado da equação
calculoEquacao = round(num1 + math.pow(num2,num3) - math.sqrt(num2) + (num1 + num2) / (num3 - num4),2)

#exibição do resultado
print('expressão: {:.2f}'.format(calculoEquacao))