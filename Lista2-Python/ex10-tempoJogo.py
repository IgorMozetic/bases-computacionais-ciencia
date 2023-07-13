# Exercício 2.10 - Tempo de Jogo

#importando a biblioteca datetime para resolução do exercício
from datetime import datetime

#enviando uma requisição ao cliente enviar o número das horas e dos minutos e início e de fim
horas1 = int(input())
minutos1 = int(input())
horas2 = int(input())
minutos2 = int(input())

#condicional para caso os dois tempos sejam iguais, o dia de finalização é alterado para o próximo, caso sejam diferentes, o dia permanece igual
if horas1 == horas2 and minutos1 == minutos2 and horas1 == minutos1:
  t1 = datetime(2022,3,27,horas1,minutos1,00)
  t2 = datetime(2022,3,28,horas2,minutos2,00)
else:
  t1 = datetime(2022,3,27,horas1,minutos1,00)
  t2 = datetime(2022,3,27,horas2,minutos2,00)
  

#calculando a diferença entre os tempos
calc = t2 - t1
tempo = str(calc)[-8:-1]

#colocando as horas e os minutos na menira solicitada
horas = tempo.split(':')[0]
minutos = tempo.split(':')[1]

#condicional para ver se já se passou pelo menos 1 dia e acrescentar na contagem de horas
if calc.days > 0:
  horas = str(calc.days*24)
if tempo.split(':')[1].startswith('0'):
  minutos = list(tempo.split(':')[1])[1]

#exibição do resultado
print(horas+"h"+minutos+'m')
