# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
# se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.


def valida(x):
  if x > 0:
    res = 'P'
  else:
    res = 'N'
  return res

entrada = int(input('Insira um número inteiro: '))

print(valida(entrada))
