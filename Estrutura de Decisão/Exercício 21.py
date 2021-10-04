# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


qnt = int(input('Qual a quantia que deseja sacar? '))
valorInicial = qnt

nota100 = qnt // 100
qnt = qnt - (nota100 * 100)

nota50 = qnt // 50
qnt = qnt - (nota50 * 50)

nota10 = qnt //  10
qnt = qnt - (nota10 * 10)

nota5 = qnt // 5
qnt = qnt - (nota5 * 5)

nota1 = qnt

if(valorInicial < 10):
  print('O valor mínimo é de 10 reais!')
elif(valorInicial > 600):
  print('O valor máximo é de 600 reais!')


else:
  if nota100 > 0:
    print('Você irá receber %i nota(s) de R$100'%(nota100))
  
  if nota50 > 0:
    print('Você irá receber %i nota(s) de R$50'%(nota50))
  
  if nota10 > 0:
    print('Você irá receber %i nota(s) de R$10'%(nota10))
  
  if nota5 > 0:
    print('Você irá receber %i nota(s) de R$5'%(nota5))
  
  if nota1 > 0:
    print('Você irá receber %i nota(s) de R$1'%(nota1))

