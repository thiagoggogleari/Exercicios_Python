# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input('Digite um número: '))

if valor > 0:
  print('O número é positivo')
elif valor < 0:
  print('O número é negativo')
else:
  print('O número 0 é neutro')