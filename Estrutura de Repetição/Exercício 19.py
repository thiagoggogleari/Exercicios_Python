# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

tamanhoConjunto = int(input('Quantos números possui o conjunto? '))
while tamanhoConjunto < 0 or tamanhoConjunto > 1000:
  print('São aceitos valores somente entre 0 e 1000')
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

