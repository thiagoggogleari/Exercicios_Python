# Faça um Programa que leia três números e mostre-os em ordem decrescente.

x = float(input('Insira o primeiro número: '))
y = float(input('Insira o segundo número: '))
z = float(input('Insira o terceiro número: '))

lista = [x,y,z]
listaOrdenada = sorted(lista)

print('Os números em ordem crescente são: ')

for i in listaOrdenada:
  print(i,' ',end='')