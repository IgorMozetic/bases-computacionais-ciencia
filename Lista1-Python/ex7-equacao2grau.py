# Exercício 1.7 - Equação do 2º Grau

import math

#enviando uma requisição ao cliente enviar o valor dos elementos da equação
a = float(input())
b = float(input())
c = float(input())
x = float(input())

#realizando o calculo para achar a primeira raiz
raiz1 = (-(b) + math.sqrt((pow(b,2) - 4*a*c)))/(2*a)

#realizando o calculo para achar a segunda raiz
raiz2 = (-(b) - math.sqrt((pow(b,2) - 4*a*c)))/(2*a)

#realizando o calculo para achar a o valor da equação
calculo = (a*pow((x),2)) + b*x + c

#exibição do resultado
print("raizes: {:.2f} {:.2f}".format(raiz1, raiz2))
print("resultado para x = {:.2f}: {:.2f}".format(x,calculo))