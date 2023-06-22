# Exercício 1.6 - Distância de Manhattan entre dois pontos

#enviando uma requisição ao cliente enviar o valor dos pontos
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

#realizando o calculo para achar a distância entre um ponto e outro
distancia = abs((x1-x2)) + abs((y1-y2))

#exibição do resultado
print('{:.4f}'.format(distancia))