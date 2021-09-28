# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados
# formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#   Dicas:
#    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#    Triângulo Equilátero: três lados iguais;
#    Triângulo Isósceles: quaisquer dois lados iguais;
#    Triângulo Escaleno: três lados diferentes;

x = float(input('Insira a primeira medida do triângulo: '))
y = float(input('Insira a segunda medida do triângulo: '))
z = float(input('Insira a terceira medida do triângulo: '))

if x == y and y == z:
  print('Triângulo Equilátero')
elif x == y or x == z or y == z:
  print('Triângulo Isósceles')
else: # Três lados diferentes
  print('Triângulo Escaleno')
