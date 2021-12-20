# Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

lista = []

for j in range(10):
  entrada = int(input('Insira o %i° elemento: '%(j+1)))
  lista.append(entrada)

soma = 0
for i in range(len(lista)):
  soma = soma + lista[i] * lista[i]

print('\nA soma dos quadrados dos elementos do vetor é de: {}'.format(soma))
