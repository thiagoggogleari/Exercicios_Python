# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
# Um número primo é aquele que é divisível apenas por um e por ele mesmo.
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

print('-- Verifica se o número é primo --')
numero = int(input('Insira um número: '))

atual = numero
anterior = numero - 1
divisoes = 0

if numero <= 0:
  print('Entrada inválida')
elif numero == 1:
  divisoes = 1
else:
  while anterior > 1:
    if atual % anterior == 0:
      divisoes += 1
    anterior -= 1

if divisoes > 0:
  print('O número %i não é primo'%(numero))
else:
  print('O número %i é primo'%(numero))
