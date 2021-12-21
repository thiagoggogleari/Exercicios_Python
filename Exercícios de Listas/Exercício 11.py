# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = ['a','b','c','d','e','f','g','h','i','j']
lista3 = [21,22,23,24,25,26,27,28,29,30]
lista4 = []

for i in range(len(lista1)):
  lista4.append(lista1[i])
  lista4.append(lista2[i])
  lista4.append(lista3[i])

print(lista4)
