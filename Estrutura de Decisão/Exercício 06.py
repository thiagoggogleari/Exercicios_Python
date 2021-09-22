1# Faça um Programa que leia três números e mostre o maior deles.

x = float(input('Insira o primeiro número: '))
y = float(input('Insira o segundo número: '))
z = float(input('Insira o terceiro número: '))

if x > y and x > z:
  print('O maior número é o',x)
elif y > x and y > z:
  print('O maior número é o',y)
elif z > y and z > x:
  print('O maior número é o',z)

elif x == y and x == z and z == x:
  print('Todos os números são iguais.')

elif x == y or x == z or y == z:
  print('Existem dois números maiores!')
