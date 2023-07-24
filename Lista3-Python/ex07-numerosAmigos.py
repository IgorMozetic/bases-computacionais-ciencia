# Exercício 3.7 - Números amigos

#enviando uma requisição ao cliente enviar os números 
numero1 = int(input())
numero2 = int(input())
soma1 = 0
soma2 = 0

# Laço de repetição para realizar o teste e imprimir se os números são amigos ou não
for cont in range(1,numero1):
  if numero1 % cont == 0:
    soma1 += cont
for cont in range(1,numero2):
  if numero2 % cont == 0:
    soma2 += cont
if soma1 == numero2 and soma2 == numero1:
  print("amigos")
else:
  print("nao amigos")