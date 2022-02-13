# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n


# Inserir aqui a quantidade de operações desejadas
n = 10

def calcula(x):
  contador = 0
  while contador < x:
    print('{} '.format(x),end='')
    contador += 1
  print()

for i in range(n):
  calcula(i+1)