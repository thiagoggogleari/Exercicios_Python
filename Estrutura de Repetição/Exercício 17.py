# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
numInicial = int(input('Deseja realizar o fatorial de qual número (n!): '))

numAtual = numInicial
numAntecessor = numInicial - 1
somatoria = 0
lista = []

# Realiza a primeira conta do fatorial
somatoria = numAtual * numAntecessor  
# Adicona o resultado a uma lista
lista.append(somatoria)

# Decrementa o número antecessor.
numAntecessor -= 1

# Enquanto o número antecessor não chega a 1 (Propriedade do fatorial)
while numAntecessor > 1:
  somatoria = somatoria * numAntecessor
  lista.append(somatoria)
  numAntecessor -= 1



# Montagem da tela de apresentação dos cálculos
print('%i! ='%(numInicial),end='')

contador = numInicial
# Este laço tenho a impressão de que podia ter sido escrito de outra maneira mais simples
for i in range(numInicial):
  if i <= numInicial -2:
    print('%i.'%contador,end='')
  else:
    print('%i='%contador,end='')
  contador -= 1
   
print('%i'%somatoria)
  
