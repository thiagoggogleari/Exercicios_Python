# Faça um programa que calcule o mostre a média aritmética de N notas. 

n = int(input('Quantas notas você deseja calcular: '))
somaTotal = 0

for i in range (n):
  nota = int(input('Insira a %i° nota: '%(i + 1)))
  somaTotal = somaTotal + nota

print('A média das notas inseridas é %.2f'%(somaTotal / n))
