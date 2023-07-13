# Exercício 2.3 - Quadrantes

#enviando uma requisição ao cliente enviar o número das duas variáveis do plano
variavelX = float(input()) 
variavelY = float(input())

#condição para entender em qual quadrante o par de variáveis se encaixa 
if variavelX == 0 and variavelY == 0:
  print('Origem')
elif variavelX == 0 and variavelY != 0:
  print('Eixo Y')
elif variavelX != 0 and variavelY == 0:
  print('Eixo X')
elif variavelX > 0 and variavelY > 0:
  print('Q1')
elif variavelX < 0 and variavelY > 0:
  print('Q2')
elif variavelX < 0 and variavelY < 0:
  print('Q3')
elif variavelX > 0 and variavelY < 0:
  print('Q4')