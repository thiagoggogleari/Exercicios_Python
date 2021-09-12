# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valorHora = float(input('Quanto você ganha por hora? '))
horasTrab = int(input('Quantas horas você trabalhou no mês? '))

print('Neste mês seu salário será de R$%.2f'%(valorHora * horasTrab))
