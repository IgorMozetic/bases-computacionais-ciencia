# Exercício 1.9 - Conversão de segundos para horas:minutos:segundos

#enviando uma requisição ao cliente enviar o valor dos segundos
entrada = int(input())

#realizando o calculo para achar as horas, os minutos e os segundos
horas = int(entrada/3600)
minutos = int((entrada%3600)/60)
segundos = int((entrada%3600)%60)

#exibição do resultado
print("%.2d:%.2d:%.2d" %(horas,minutos,segundos))