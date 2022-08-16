#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 
altura = float(input('Insira sua altura em m: '))
homem = (72.7 * altura) - 58
mulher = (62.1 * altura) - 44.7
print(f'Seu peso ideal para homem é de {homem} e para mulher {mulher}')