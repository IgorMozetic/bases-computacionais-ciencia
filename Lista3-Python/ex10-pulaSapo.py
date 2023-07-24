# Exercício 3.10 - Pula Sapo

#enviando uma requisição ao cliente enviar o número de pulo do sapo e o número de canos 
puloSapo = int(input())
numCanos = int(input())
canoAntigo = 0

# Laço de repetição para realizar a contagem se o sapo consegue ou não pular os canos
for cont in range(0,numCanos):
  alturaCano = int(input())
  if canoAntigo != 0:
    if canoAntigo + puloSapo < alturaCano or canoAntigo - puloSapo > alturaCano:
      condicao = False
      break
    else:
      condicao = True
  canoAntigo = alturaCano
if condicao:
  print("YOU WIN")
else:
  print("GAME OVER")