# Exercício 3.9 - Falha do motor

#enviando uma requisição ao cliente enviar o número de medições do RPM
qntMedicoes = int(input())
rpmAntigo = 0
queda = 0

# Laço de repetição para identificar se caso houve alguma queda de RPM e imprimir 
for cont in range(1,qntMedicoes+1):
  rpm = int(input())
  if rpm < rpmAntigo:
    if queda == 0:
      queda = cont
  rpmAntigo = rpm
print(queda) 