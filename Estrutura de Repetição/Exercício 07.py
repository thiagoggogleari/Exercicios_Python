# Faça um programa que leia 5 números e informe o maior número.

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))
n4 = int(input('Insira o quarto número: '))
n5 = int(input('Insira o quinto número: '))
print()

maior = 0
tupla = (n1,n2,n3,n4,n5)

for i in range(5):
  
  if tupla[i] > maior:
    maior = tupla[i]

print('O maior número inserido é %i'%(maior))
