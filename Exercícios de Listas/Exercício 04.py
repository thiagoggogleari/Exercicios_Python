# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes.

lista = []

for i in range(10):
  entrada = input('Insira o %i° caractere: '%(i + 1))
  lista.append(entrada)

vogais = ['A','E','I','O','U']
posicaoVogais = []

for i in range(len(lista)):
  if(lista[i].upper() in vogais):
    posicaoVogais.append(i)

print('\nLista: ',end='')
for i in range(len(lista)):
  if i < len(lista) - 1:
    print(lista[i],", ",end='')
  else:
    print(lista[i],".")

# Total de caracteres, menos a quantidade de vogais
qntConsoantes = len(lista) - len(posicaoVogais)
print('\nExistem %i consoantes na lista'%(qntConsoantes))
