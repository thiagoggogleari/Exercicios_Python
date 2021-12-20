# Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser
# compostos pelos elementos intercalados dos dois outros vetores.

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = ['a','b','c','d','e','f','g','h','i','j']
lista3 = []

for i in range(len(lista1)):
  lista3.append(lista1[i])
  lista3.append(lista2[i])

print(lista3)
