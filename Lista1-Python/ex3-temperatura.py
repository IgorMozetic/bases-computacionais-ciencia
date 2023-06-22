# Exercício 1.2 - paralelepipedo

#enviando uma requisição ao cliente enviar a temperatura em celsius
temperaturaCelsius = float(input())

#realizando o calculo para achar a temperatura em Fahrenheit e Kelvin
temperaturaFahrenheit = int(temperaturaCelsius * (9 / 5) + 32)
temperaturaKelvin = int(temperaturaCelsius + 273)

#exibição do resultado
print(temperaturaFahrenheit, 'F')
print(temperaturaKelvin, 'K')