# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []

for i in range(5):
  inputLista = int(input('Insira o %i° valor da lista: '%(i+1)))
  lista.append(inputLista)


print('\nA lista é composta por: ',end='')

for i in range(len(lista)):
  
  if(i < len(lista) -1):
    print('%i, '%(lista[i]),end='')
  else:
     print('e %i.'%(lista[i]))

print('Vetor: ',lista)
