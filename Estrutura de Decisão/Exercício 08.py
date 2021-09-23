# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input('Qual o preço do primeiro produto: '))
produto2 = float(input('Qual o preço do segundo produto: '))
produto3 = float(input('Qual o preço do terceiro produto: '))

if produto1 < produto2 and produto1 < produto3:
  print('Você deve comprar o produto 1')
elif produto2 < produto1 and produto2 < produto3:
  print('Você deve comprar o produto 2')
elif produto3 < produto1 and produto3 < produto2:
  print('Você deve comprar o produto 3')

if produto1 == produto2 and produto1 == produto3:
  print('O preços dos 3 produtos são iguais')
elif produto1 == produto2 and produto1 < produto3:
  print('Produto 1 e produto 2 têm o mesmo preço e são menores que o produto 3')
elif produto1 == produto3 and produto1 < produto2:
  print('Produto 1 e produto 3 têm o mesmo preço e são menores que o produto 2')
elif produto2 == produto3 and produto2 < produto1:
  print('Produto 2 e produto 3 têm o mesmo preço e são menores que o produto 1')