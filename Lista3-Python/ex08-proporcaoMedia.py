# Exercício 3.8 - Proporção de adultos e média das idades

#importando a biblioteca math para resolução do exercício
import math

#enviando uma requisição ao cliente enviar o número de pessoas
numero = int(input())
soma = 0
proporcao = 0

# Laço de repetição para realizar a média e a proporção de pessoas adultas
for cont in range(1,numero+1):
  idade = int(input())
  soma += idade
  if idade >= 18:
    proporcao += 1
print("{:.1f}%".format((proporcao/numero)*100))
print("{:.1f}".format(soma/numero))