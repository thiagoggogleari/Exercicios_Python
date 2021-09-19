# Faça um Programa que peça dois números e imprima o maior deles.

x = float(input('Insira um número: '))
y = float(input('Insira outro número: '))

if x > y:
  print('O maior número é {}'.format(x))
elif x < y:
  print('O maior número é {}'.format(y))
else:
  print('Os números digitados são iguais!')
