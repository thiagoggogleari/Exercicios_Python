
# Faça um programa que leia uma quantidade indeterminada de números positivos e conte
# quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
# A entrada de dados deverá terminar quando for lido um número negativo.

contLista1 = 0 # [0-25]
contLista2 = 0 # [26-50]
contLista3 = 0 # [51-75]
contLista4 = 0 # [76-100]

while True: 
  entrada = float(input('Insira um número: '))

  if entrada < 0:
    break
  
  if entrada >= 0 and entrada <=25:
    contLista1 += 1
  if entrada >= 26 and entrada <= 50:
    contLista2 += 1
  if entrada >= 51 and entrada <= 75:
    contLista3 += 1
  if entrada >= 76 and entrada <= 100:
    contLista4 += 1


print('Intervalo [0-25] possui: %i registros'%(contLista1))
print('Intervalo [26-50] possui: %i registros'%(contLista2))
print('Intervalo [51-75] possui: %i registros'%(contLista3))
print('Intervalo [76-100] possui: %i registros'%(contLista4))