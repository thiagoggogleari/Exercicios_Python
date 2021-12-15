# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores.

vetorTotal = []
vetorPar = []
vetorImpar = []

for i in range(20):
  entrada = int(input('Insira o %i° número inteiro: '%(i+1)))
  vetorTotal.append(entrada)

for i in range(len(vetorTotal)):
  if vetorTotal[i] % 2 == 0:
    vetorPar.append(vetorTotal[i])
  else:
    vetorImpar.append(vetorTotal[i])

print('Vetor Total: ',vetorTotal)
print('Vetor Par: ',vetorPar)
print('Vetor Ímpar: ',vetorImpar)
