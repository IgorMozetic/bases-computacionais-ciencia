# Exercício 2.9 - Árvore de Decisão para Jogar Tênis

#enviando uma requisição ao cliente enviar o aspecto, a umidade e o vento
aspecto = input()
umidade = input()
vento = input()

#condição para testar se será possível jogar tenis
if aspecto == "Sol":
  if umidade == "Elevada":
    print("N")
  if umidade == "Normal":
    print("S")
elif aspecto == "Nuvens":
  print("S")
elif aspecto == "Chuva":
  if vento == "Fraco":
    print("S")
  elif vento == "Forte":
    print("N")
    
