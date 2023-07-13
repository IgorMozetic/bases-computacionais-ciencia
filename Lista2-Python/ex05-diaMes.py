# Exercício 2.5 - Quantidade de dias do mês

#lista com todos os dias de todos os meses mapeados pelo professor no exercício
meses = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

#função para identificar qual a quantidade de dias no mês que foi enviado
def funcaoDiaMes(mes):
  #tente fazer isso, caso haja erro, execute o except
  try:
    meses[mes]
    print(meses[mes])
  except:
    print(0)
    
#enviando uma requisição ao cliente enviar o número referente ao mês
funcaoDiaMes(int(input()))