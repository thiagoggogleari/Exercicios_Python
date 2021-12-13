# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

listaNotas = []

# Adiciona elementos à lista
for i in range(4):
  notas = float(input('Insira a %i° nota: '%(i+1)))
  listaNotas.append(notas)

# Realiza a soma de todos os elementos
totalNotas = 0
for i in range(len(listaNotas)):
  totalNotas = totalNotas + listaNotas[i]

# Calcula a média com base no tamanho da lista de notas
media = totalNotas / len(listaNotas)
print('\nA média de notas é de %.2f'%(media))
