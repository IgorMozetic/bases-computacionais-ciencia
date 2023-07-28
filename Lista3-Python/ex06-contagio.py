# Exercício 3.6 - Contágio

#enviando uma requisição ao cliente enviar o número da população, da quantidade de pessoas infectadas no dia 0, a taxa de contágio e a porcentagem de imunidade
populacao = int(input())
qntDia0 = int(input())
txContagio = float(input())
imunidade = int(input())
pessoasInfectadas = 0
contagemPessoas = 0
cont = 0

# Laço de repetição para verificar se a quantidade de pessoas infectadas é superior a taxa de imunidade
while (contagemPessoas/populacao*100) < imunidade:
    if imunidade <= round((contagemPessoas*txContagio/populacao)*100):
        print(cont)
        break
    if pessoasInfectadas != 0:
        pessoasInfectadas = (pessoasInfectadas*txContagio)
        contagemPessoas += pessoasInfectadas
    else:
        pessoasInfectadas = qntDia0
        contagemPessoas = qntDia0
    cont+=1
