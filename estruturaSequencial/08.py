#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 
salarioPorHora = int(input('Insira o seu salario por hora: '))
numeroDeHorasTrabalhadasNoMes = int(input('Insira as horas trabalhadas: '))
salarioMensal = (salarioPorHora * numeroDeHorasTrabalhadasNoMes)
print(f'O seu salário mensal é de: {salarioMensal}')