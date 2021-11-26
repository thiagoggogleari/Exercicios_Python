# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por 
# meio de código. Os códigos utilizados são:

# 1 , 2, 3, 4  - Votos para os respectivos candidatos 
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco

# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

nulo = 0
branco = 0

listaCandidatos = [0,0,0,0,0,0]

print('Candidato 1: João')
print('Candidato 2: José')
print('Candidato 3: Jairo')
print('Candidato 4: Joaquim\n')

while True:
  desejaVotar = input('\nRealizar votação? [S/N]')
  
  if desejaVotar.upper() == 'N':
    break
  elif desejaVotar.upper() == 'S':
    
    print('Código dos candidatos: 1/2/3/4')
    print('Para votar nulo digite 5 e para votar em branco digite 6')
    voto = int(input('Insira seu voto: '))

    while voto < 1 or voto > 6:
      print('Verifique o número e tente novamente.\n')
      print('Para votar nulo digite 5, para votar em branco digite 6')
      voto = int(input('Insira seu voto: '))
    
    listaCandidatos[voto - 1] = listaCandidatos[voto - 1] + 1 #Desloca 1 posição para esquerda


# Lista completa dos votos
# print('\nListaCandidatos = {}'.format(listaCandidatos))

print('\n---- Resultado da votação ----')
print('\nCandidato João obteve: {}'.format(listaCandidatos[0]))
print('Candidato José obteve: {}'.format(listaCandidatos[1]))
print('Candidato Jairo obteve: {}'.format(listaCandidatos[2]))
print('Candidato Joaquim obteve: {}'.format(listaCandidatos[3]))
print('Votos nulos: {}'.format(listaCandidatos[4]))
print('Votos em branco: {}'.format(listaCandidatos[5]))


totalVotos = 0
for i in range (6):
  totalVotos = totalVotos + listaCandidatos[i]

print('\nTotal de votos: {}'.format(totalVotos))


# Condição necessário para que não ocorra divisão por zero nos cálculos de porcentagem
if totalVotos != 0:
  totalVotosNulos = listaCandidatos[4]
  totalVotosBranco = listaCandidatos[5]

  nulosSobreTotal = (totalVotosNulos * 100) / totalVotos
  print('A porcentagem de nulos sobre o total de votos é de {:.2f}%'.format(nulosSobreTotal))

  brancoSobreTotal = (totalVotosBranco * 100) / totalVotos
  print('A porcentagem de branco sobre o total de votos é de {:.2f}%'.format(brancoSobreTotal))
