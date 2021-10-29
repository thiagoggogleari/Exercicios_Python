# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
# limitando o fatorial a números inteiros positivos e menores que 16.

while True:
  numInicial = int(input('Deseja realizar o fatorial de qual número (n!): '))

  while numInicial < 0 or numInicial > 15:
    print('Número deve ser entre 0 e 15!')
    numInicial = int(input('Deseja realizar o fatorial de qual número (n!): '))

  lista = []
  numAtual = numInicial
  numAntecessor = numInicial - 1

  while numAntecessor > 1:
    numAtual = numAtual * numAntecessor
    lista.append(numAtual)
    numAntecessor -= 1

  # Mostra a lista que foi montada, com os resultado dos cálculos
  # print(lista)

  # Montagem da tela de apresentação dos cálculos
  print('%i!= '%(numInicial),end='')

  contador = numInicial

  # Propriedade de fatorial de 0! e 1!, tem resultado 1
  if numInicial == 0 or numInicial == 1:
    print('1')
  else:
  # Apresenta na tela os fatores
    for i in range(numInicial):
      if i <= numInicial -2:
        print('%i.'%contador,end='')
      else:
        print('%i = '%contador,end='')
      contador -= 1
      
    print('%i'%numAtual)
