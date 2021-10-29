# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

numero = 1

for i in range (20):
  print(numero)
  numero += 1

numero = 1

for j in range (20):
  print(numero,end='')
  numero += 1
