# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando
# o número do aluno e o segundo representando a sua altura em centímetros. Encontre 
# o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do
# aluno mais baixo, junto com suas alturas.


# A altura é gerada 'randomicamente' e o número do aluno é sequencial
# O código não verifica caso tenham alunos com a mesma altura

import random
dicionario = {'Número':[],'Altura':[]}

dicionario['Número'].append(1)
psAleatorio = random.randrange(150, 210, 1)
dicionario['Altura'].append(psAleatorio)

# Variáveis
maisBaixo = psAleatorio
maisAlto = psAleatorio
indiceMaisBaixo = 0
indiceMaisAlto = 0

for i in range(9):
  dicionario['Número'].append(i + 2)
  psAleatorio = random.randrange(150, 210, 1)
  dicionario['Altura'].append(psAleatorio)
  
  if dicionario['Altura'][i] < maisBaixo:
    maisBaixo = dicionario['Altura'][i]
    indiceMaisBaixo = i
  elif dicionario['Altura'][i] > maisAlto:
    maisAlto = dicionario['Altura'][i]
    indiceMaisAlto = i
    
for i,j in dicionario.items():
  print(i,j)

print()
print('Mais baixo: %icm'%(maisBaixo))
print('Seu número de registro é: %i'%(dicionario['Número'][indiceMaisBaixo]))
# print('Índice mais baixo: %i'%(indiceMaisBaixo))
print()

print('Mais alto: %icm'%(maisAlto))
print('Seu número de registro é: %i'%(dicionario['Número'][indiceMaisAlto]))
# print('ìndice mais alto: %i'%(indiceMaisAlto))
