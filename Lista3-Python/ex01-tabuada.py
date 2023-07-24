# Exercício 3.1 - Tabuada

# enviando uma requisição ao cliente enviar o número da tabuada e o número máximo das multiplicações
n = int(input())
m = int(input())

# Laço de repetição para imprimir a tabuada
for cont in range(0,m+1):
  print("{:n} x {:n} =".format(n,cont),n*cont)