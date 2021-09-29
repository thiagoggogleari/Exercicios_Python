#   Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c
#   e fazer as consistências, informando ao usuário nas seguintes situações:
#   Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo 
#    encerrado;
#    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

from math import sqrt

a = float(input('Insira o valor de a: '))
if a == 0:
  print('Equação não é de segundo grau!')
else:
  b = float(input('Insira o valor de b: '))
  c = float(input('Insira o valor de c: '))
  print()
  delta = b**2 - 4 * a * c 
  print('*'*40)

  if delta < 0:
    print('A equação não possui raízes reais!')
  else:
    x1 = (-b + (sqrt(delta)))/(2 * a)
    x2 = (-b - (sqrt(delta)))/(2 * a)

    print('Aplicando a fórmula de Baskara')
    print('*'*40)

    if delta == 0:
      print('Existe apenas umas raíz real que é: ',x1)
    else:
      print()
      print('O valor x1 é: ', x1)
      print('O valor x2 é: ', x2) 
  print('*'*40)