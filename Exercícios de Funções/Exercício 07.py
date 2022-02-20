# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números. 

lista = [2,4,5,6,7]

def soma(lista):
  resultado = 0
  for i in range(len(lista)):
    resultado += lista[i]
  return resultado
  
def multiplicacao(lista):
  resultado = 1
  for i in range(len(lista)):
    resultado = resultado * lista[i]
  return resultado

print('Os números da lista são: ')
for i in range(len(lista)):
  if i < (len(lista) -1):
    print('{}, '.format(lista[i]),end='')
  else:
    print('{}.'.format(lista[i]))
  
print('\nSoma: ',soma(lista))
print('Multiplicação: ',multiplicacao(lista))
