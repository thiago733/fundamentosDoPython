#Faça um Programa que peça as 4 notas bimestrais e mostre a média. 
notaPrimeiroBimestre = int(input('Insira a primeira nota: '))
notaSegundoBimestre = int(input('Insira a segunda nota:  '))
notaTerceiroBimestre = int(input('Insira a terceira nota: '))
notaQuartoBimestre = int(input('Insira a quarta nota: '))
media = (notaPrimeiroBimestre + notaSegundoBimestre + notaTerceiroBimestre + notaQuartoBimestre)/4 
print (f'A media das notas é: {media}')