# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.

print('--== Sequência de Fibonacci ==--')

x = 1 # Posição 1
y = 0 # Posição 2
z = 0 # Resultado da operação


print('0')

while z <= 500: 
  z = x + y
  print(z) 
  # Realiza o deslocamento das variáveis para a direita, ou seja,
  # as variáveis abaixo assumem os valores das variáveis ao lado.
  x = y
  y = z
