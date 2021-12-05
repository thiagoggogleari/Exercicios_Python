#  Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
#  No final da série de saltos de cada atleta, o melhor e o pior resultados são
#  eliminados. O seu resultado fica sendo a média dos três valores restantes. 

#  Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas 
#  pelo atleta em seus saltos e depois informe a média dos saltos conforme a
#  descrição acima informada (retirar o melhor e o pior salto e depois calcular 
#  a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados
#  na ordem da execução, portanto não são ordenados. O programa deve ser encerrado
#  quando não for informado o nome do atleta. A saída do programa deve ser conforme
#  o exemplo abaixo:

# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m

# Resultado final:
# Rodrigo Curvêllo: 5.9 m 

while True:  
  distancias = []
  nomeCompetidor = input('\nQual o nome do jogador? ')
  
  if nomeCompetidor == '':
    print('Programa Finalizado!')
    break

  for i in range(5):
    distanciaCompetidor = float(input('Qual a distância do %i° salto? '%(i+1)))
    distancias.append(distanciaCompetidor)

  print('\nAtleta: %s'%(nomeCompetidor))
  print('\nPrimeiro Salto: %.1f m'%(distancias[0]))
  print('Segundo Salto: %.1f m'%(distancias[1]))
  print('Terceiro Salto: %.1f m'%(distancias[2]))
  print('Quarto Salto: %.1f m'%(distancias[3]))
  print('Quinto Salto: %.1f m'%(distancias[4]))

  # Cria uma nova lista ordenada
  listaOrdenada = sorted(distancias)
                  
  print('\nMelhor Salto: %.1f m'%(listaOrdenada[4]))
  print('Pior Salto: %.1f m'%(listaOrdenada[0]))

  # Apaga primero e último registro
  del(listaOrdenada[4])
  del(listaOrdenada[0])

  # Cálculo da média (Desconsiderando melhor e pior resultado)
  totalMedia = 0
  for i in range(3):
    totalMedia = totalMedia + listaOrdenada[i]
  media = totalMedia / 3
    
  print('Média dos demais saltos: %.1f m'%(media))

  print('\nResultado final: ')
  print('%s: %.1f m'%(nomeCompetidor,media))
