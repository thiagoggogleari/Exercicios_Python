# Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 

n = int(input('Quantos termos deseja vizualizar?'))

dividendo = 1
divisor = 1

print('S = ',end='')

for i in range(n):
  print('%i/%i'%(dividendo,divisor),end='')
  dividendo += 1
  divisor += 2

  if i != n-1:
    print(' + ',end='')
