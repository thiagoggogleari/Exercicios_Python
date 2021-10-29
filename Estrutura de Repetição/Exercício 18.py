# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

tamanhoConjunto = int(input('Quantos números possui o conjunto? '))
# Lista aonde será armazenados os valores do conjunto
lista = []

# Solicita os valores de acordo com o tamanho do conjunto
for i in range(tamanhoConjunto):
  valor = int(input('Digite o número de posição %i: '%(i + 1))) # pula posição 0
  # Vai adicionando à lista
  lista.append(valor)


tamanhoLista = len(lista) -1

# Organiza a lista em ordem numérica
lista.sort()

print('O menor número é %i'%(lista[0]))
print('O maior número é %i'%(lista[tamanhoLista]))


soma = 0
for i in lista:
  soma = soma + i
print('A soma de todos os números é: %i'%(soma))
