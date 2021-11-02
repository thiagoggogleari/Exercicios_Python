# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

print('-- Lista de candidatos --')
print('1 - Machado de Assis')
print('2 - George Orwell')
print('3 - Starman')

candidato1 = 0
candidato2 = 0
candidato3 = 0

eleitores = int(input('Quantas pessoas irão votar? '))

for i in range(eleitores):
  entrada = int(input('Eleitor %i insira seu voto: '%(i + 1)))
  while entrada not in (1,2,3):
    print('Entrada inválida.')
    entrada = int(input('Eleitor %i insira seu voto: '%(i + 1)))

  print('Voto computado')
  print()

  if(entrada == 1):
    candidato1 += 1
  elif(entrada == 2):
    candidato2 += 1
  else:
    candidato3 += 1

print('Quantidade de votos: ')
print('Candidato 1 = %i'%(candidato1))
print('Candidato 2 = %i'%(candidato2))
print('Candidato 3 = %i'%(candidato3))
