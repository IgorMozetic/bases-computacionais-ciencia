# Exercício 3.3 - Jogo do PIM

#enviando uma requisição ao cliente enviar o número de PIMS
numero = int(input())

# Laço de repetição para imprimir os números e o PIM nos múltiplos de 4
for cont in range(1,(numero*4)+1):
  if cont % 4 == 0:
    print("PIM")
  else:
    print(cont)