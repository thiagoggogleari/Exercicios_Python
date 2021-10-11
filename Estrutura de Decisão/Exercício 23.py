# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

x = float(input('Insira um número: '))

arr = round(x,0)

if arr == x:
  print('É um número inteiro')
else:
  print('É um número decimal')
