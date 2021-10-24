# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.

print('Sequência de Fibonacci')
numFinal = int(input('Insira a quantia de cálculos a serem feitos: '))


x = 1 # Posição 1
y = 0 # Posição 2
z = 0 # Resultado da operação

print('--== Sequência de Fibonacci ==--')

for i in range(numFinal):
  z = x + y
  print(z) 
  # Realiza o deslocamento das variáveis para a direita, ou seja,
  # as variáveis abaixo assumem os valores das variáveis ao lado.
  x = y
  y = z
