# Exercício 1.5 - Parcelamento

#enviando uma requisição ao cliente enviar o valor da venda e as parcelas
entrada = float(input())
parcelas = int(input())

#realizando o calculo para achar o valor das parcelas
valorParcela = entrada / parcelas

#exibição do resultado
print('R$ {:.2f}'.format(valorParcela))