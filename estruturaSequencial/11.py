#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo. 
primeiroNumero = int(input('Insira o primeiro número: '))
segundoNumero = int(input('Insira o segundo número: '))
terceiroNumero = int(input('Insira o terceiro número: '))
primeroResultado = (2 * primeiroNumero) * (segundoNumero / 2)
segundoResultado = (3 * primeiroNumero) + (terceiroNumero)
terceiroResultado =  (terceiroNumero * terceiroNumero * terceiroNumero)
print(f'O primeiro resultado é: {primeroResultado}')
print(f'O primeiro resultado é: {segundoResultado}')
print(f'O primeiro resultado é: {terceiroResultado}')