# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = []

for i in range(5):
  entrada = int(input('Insira o número real de posição %i: '%(i+1)))
  vetor.append(entrada)

# É criado uma cópia para manipulação, assim o vetor original se mantém
copiaVetor = vetor.copy()
copiaVetor.sort()
copiaVetor.reverse()

print('\nLista montada= ',end='')
for j in range (len(vetor)):
    if j < len(vetor) -1:
      print('%i, '%(vetor[j]),end='')
    else:
      print('%i.'%(vetor[j]))


print('\nOrdem inversa= ',end='')
for j in range (len(copiaVetor)):
    if j < len(copiaVetor) -1:
      print('%i, '%(copiaVetor[j]),end='')
    else:
      print('%i.'%(copiaVetor[j]))
