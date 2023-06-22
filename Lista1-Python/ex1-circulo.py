# Exercício 1.1 - Área do círuclo

#importando a biblioteca math para utilização de suas funções
import math

#enviando uma requisição ao cliente enviar o número da área do círculo
entrada = float(input())

#realizando o calculo para achar a a área do círculo
calculo_area = math.pi * pow(entrada, 2)

#exibição do resultado
print('{:.4f}'.format(calculo_area))