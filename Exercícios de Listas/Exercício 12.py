# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos
# alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.


import random
idades = []
alturas = []

# Gera duas listas de tamanho 30,com valores aleatórios para idade (entre 14 e 26) e altura (entre 1.50 e 2.10)
for i in range(30):
  geraIdade = random.randint(14,26)
  idades.append(geraIdade)

  geraAltura = random.uniform(1.5,2.1)
  geraAltura = round(geraAltura,2)
  alturas.append(geraAltura)

# Cálculo da média
somaAlturas = 0
for i in range(len(alturas)):
  somaAlturas = somaAlturas + alturas[i]

media = somaAlturas / len(alturas)

# Verifica a qntd de maiores de 13 abaixo da média
alunosMaior13 = 0
for i in range(len(idades)):
  if idades[i] > 13 and alturas[i] < media:
    alunosMaior13 += 1

print(idades)
print(alturas)

print('\n\nA média de altura é de %.2f'%(media))
print('Existem %i alunos acima de 13 anos que estão abaixo da média de altura'%(alunosMaior13))
