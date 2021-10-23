# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

lista = []
pares = 0
impares = 0
contNulos = 0

for i in range(10):
    # Vai preenchendo a lista com os números inseridos
    i = int(input('%i de 10 - Insira um número: '%(i+1)))
    lista.append(i) 

# Verifica se o número é par ou ímpar e incrementa uma variável
tamanhoLista = len(lista)
for j in range(tamanhoLista) :
  
  if lista[j] == 0:
    contNulos += 1
  elif lista[j] % 2 == 0:
    pares += 1
  else:
    impares += 1

print('\nNúmeros:')
print('Par = %i'%(pares))
print('Ímpar = %i'%(impares))

if(contNulos > 0):
  print('Nulo = %i'%(contNulos))
