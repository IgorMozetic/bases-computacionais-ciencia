# Exercício 3.4 - Contagem regressiva maluca

#enviando uma requisição ao cliente enviar a quantidade de tempo restante
tempo = int(input())
restante = tempo

# Laço de repetição para imprimir a quantidade de segundos que faltam por múltiplos de 2
for cont in range(0,tempo+1):
  if cont == 0:
    print("Faltam {:n} segundos".format(tempo))
  else:
    restante = restante-(cont*2)
    print("Faltam {:n} segundos".format(restante))
  if restante-(cont*2) <= 0:
    print("Acabou")
    break
  