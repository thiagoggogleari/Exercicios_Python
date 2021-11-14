# Foi feita uma estatística em cinco cidades brasileiras para coletar dados 
# sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# - Código da cidade;
# - Número de veículos de passeio (em 1999);
# - Número de acidentes de trânsito com vítimas (em 1999).

#  Deseja-se saber:
# - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# - Qual a média de veículos nas cinco cidades juntas;
# - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

listaCidades = []
listaVeiculos = []
listaAcidentes = []

# Como no exercício não foi informado os dados, foi inserido uma tela de cadastro
for i in range(5):
  cidade = input('Insira o nome da %i° cidade: '%(i +1))
  listaCidades.append(cidade)

  veiculosPasseio = int(input('Insira a quantidade de veículos de passeio da %i° cidade: '%(i+1)))
  listaVeiculos.append(veiculosPasseio)

  acidentes = int(input('Insira a quantidade de acidentes na %i° cidade: '%(i+1)))
  listaAcidentes.append(acidentes)
  print()


tamanhoLista = len(listaCidades)
listaOrdenadaAcidentes = sorted(listaAcidentes)
menorAcidentes = listaOrdenadaAcidentes[0]
maiorAcidentes = listaOrdenadaAcidentes[tamanhoLista -1]

# Faz uma varredura e registra na variável a 'posição na lista' do menor e maior número de acidentes
for j in range(tamanhoLista):
  if listaAcidentes[j] < maiorAcidentes:
    posicaoMenorAcidentes = j
    menorAcidentes = listaAcidentes[j] # posicão na lista
  elif listaAcidentes[j] > menorAcidentes:
    posicaoMaiorAcidentes = j
    maiorAcidentes = listaAcidentes[j] # posição na lista

print('\nA cidade com menor índice de acidentes é %s'%(listaCidades[posicaoMenorAcidentes]))
print('Com {} acidentes'.format(listaAcidentes[posicaoMenorAcidentes]))

print('\nA cidade com maior índice de acidentes é %s'%(listaCidades[posicaoMaiorAcidentes]))
print('Com {} acidentes'.format(listaAcidentes[posicaoMaiorAcidentes]),'\n')


# Cálculo da média
totalAcidentes = 0
totalAbaixo2000 = 0

for i in range(tamanhoLista):
  totalAcidentes = totalAcidentes + listaAcidentes[i]
  if listaVeiculos[i] < 2000:
    totalAbaixo2000 = totalAbaixo2000 + listaVeiculos[i]

print('A média de acidentes entre todas as cidades é de %.2f acidentes.\n'%(totalAcidentes / tamanhoLista))

if totalAbaixo2000 == 0:
  print('Não há cidades com menos de 2000 veículos em sua frota.')
else:
  print('Em cidades com menos de 2000 veículos a média é de: %.2f acidentes'%(totalAbaixo2000 / tamanhoLista))

# print(listaCidades)
# print(listaVeiculos)
# print(listaAcidentes)
