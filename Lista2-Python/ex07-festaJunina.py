# Exercício 2.7 - Festa Junina

#lista com todos os produtos mapeados pelo professor no exercício da festa junina
produtos = {
    1:8,
    2:6,
    3:7,
    4:5,
    5:3,
    6:5,
    7:5,
    8:5,
    9:4,
    10:4
}

#função para identificar qual foi o valor do pedido solicitado pelo cliente
def pedidoFesta(produto,quantidade):
  #tente fazer isso, caso haja erro, execute o except
  try:
    produtos[produto]
    #condiconal para ver se a quantidade solicitada é válida
    if quantidade > 0:
      valor = produtos[produto] * quantidade
      print('R${:.2f}'.format(valor))
    else:
      print('quantidade invalida')
  except:
    print('pedido invalido')
    
#enviando uma requisição ao cliente enviar o pedido e a quantidade
produto = int(input())
quantidade = int(input())
pedidoFesta(produto,quantidade)