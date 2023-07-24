# Exercício 3.2 - Máquina de Somar

#enviando uma requisição ao cliente enviar o número de quantidade de números da soma
numero = int(input())
soma = 0

# Laço de repetição para imprimir a soma dos números enviados
for cont in range(0,numero): 
  soma += float(input())
print("Total: {:.2f}".format(soma))
