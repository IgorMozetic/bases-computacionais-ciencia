# Exercício 1.8 - Salário com bônus

#enviando uma requisição ao cliente enviar o nome, o salário o total de vendas e a comissão
nome = input()
salarioFixo = float(input())
totalVendas = float(input())
comissao = int(input())

#realizando o calculo para o bônus
bonus = salarioFixo + (totalVendas * (comissao/100))

#exibição do resultado
print('{} deve receber R$ {:.2f}'.format(nome,bonus))