# Exercício 2.1 - DDD

#lista com todos os estados mapeados pelo professor no exercício
estados = {
    61:'Brasilia',
    71:'Salvador',
    11:'Sao Paulo',
    21:'Rio de Janeiro',
    32:'Juiz de Fora',
    19:'Campinas',
    27:'Vitoria',
    31:'Belo Horizonte'
}

#função para identificar qual o ddd que foi enviado
def funcaoDDD(ddd):
  #tente fazer isso, caso haja erro, execute o except
  try:
    estados[ddd]
    print(estados[ddd])
  except:
    print('DDD nao cadastrado')
    
#enviando uma requisição ao cliente enviar o número de ddd
funcaoDDD(int(input()))