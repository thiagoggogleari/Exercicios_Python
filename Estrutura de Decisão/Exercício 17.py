# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input('Insira o número equivalente a um ano: '))

if(ano % 4 == 0):
  print('É um ano bissexto')
else:
  print('Não é um ano bissexto')