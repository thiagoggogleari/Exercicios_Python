# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor.
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para
# gerar numeros aleatórios, simulando os lançamentos dos dados.

import random

def numAleatorio():
  x = random.randint(1,6)
  return x

valoresDados = []

for i in range(100):
  valoresDados.append(numAleatorio())

print('Simulador de lançamento de dados (100x)\n')
for i in range(6):
  print('O número {} apareceu {} vezes'.format(i+1, valoresDados.count(i+1)))
