# Faça um Programa que leia um vetor de 5 números inteiros,
# mostre a soma, a multiplicação e os números.

lista = []

for i in range(5):
  entrada = int(input('Insira o %i° número inteiro da lista: '%(i+1)))
  lista.append(entrada)

soma = 0
mult = 1

for i in lista:
  soma = soma + i
  mult = mult * i

print('\nLista: ',end='')
for i in range(len(lista)):
  if i < len(lista) -1:
    print(lista[i],', ',end='')
  else:
    print(lista[i],'.')

print('A soma dos numéros é = %i'%(soma))
print('A multiplicação dos números é = %i'%(mult))
