# Exercício 3.5 - É Fatorial?

#importando a biblioteca math para resolução do exercício
import math

#enviando uma requisição ao cliente enviar o número 
numero = int(input())

# Laço de repetição para realizar o teste e imprimir se o número é fatorial ou não
for cont in range(0,numero+1):
  fatorial = math.factorial(cont)
  if fatorial == numero:
    condicao = True
    break
  else:
    condicao = False
  if(fatorial > numero):
    condicao = False
    break
if condicao == True:
  print('Verdadeiro')
else:
  print('Falso')
  