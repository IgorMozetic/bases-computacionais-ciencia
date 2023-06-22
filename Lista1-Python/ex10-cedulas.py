# Exercício 1.10 - Cédulas

#enviando uma requisição ao cliente enviar o valor completo do dinheiro
entrada = int(input())

#realizando o calculo para achar a quantidade de nota para cada cédula
notas100 = entrada//100
entrada = entrada%100
notas50 = entrada//50
entrada = entrada%50
notas20 = entrada//20
entrada = entrada%20
notas10 = entrada//10
entrada = entrada%10
notas5 = entrada//5
entrada = entrada%5
notas2 = entrada//2
notas1 = entrada%2

#exibição do resultado
print('{} de 100, {} de 50, {} de 20, {} de 10, {} de 5, {} de 2, {} de 1'.format(notas100,notas50,notas20,notas10,notas5,notas2,notas1))