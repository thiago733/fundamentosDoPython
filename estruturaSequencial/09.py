#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 
#C = 5 * ((F-32) / 9). 
temperaturaEmFahrenheit = int(input('Insira a temperatura em Fahrenheit: '))
temperaturaEmCelsius = 5 * ((temperaturaEmFahrenheit - 32) / 9)
print(f'A temperatura em Fahreinheit é: {temperaturaEmCelsius}')