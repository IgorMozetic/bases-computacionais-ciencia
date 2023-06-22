# Exercício 1.2 - paralelepipedo

#importando a biblioteca math para utilização de suas funções
import math

#enviando uma requisição ao cliente enviar os número das arestas
aresta1 = float(input())
aresta2 = float(input())
aresta3 = float(input()) 

#realizando o calculo para achar a o volume e a diagonal
volume_paralelepipedo = round(aresta1 * aresta2 * aresta3,2)
diagonal_paralelepipedo = round(math.sqrt(pow(aresta1, 2) + pow(aresta2, 2) + pow(aresta3, 2)),2)

#exibição do resultado
print('Volume: {:.2f}'.format(volume_paralelepipedo), 'Diagonal: {:.2f}'.format(diagonal_paralelepipedo))