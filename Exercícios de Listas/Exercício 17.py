# Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# O resultado do atleta será determinado pela média dos cinco valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
# pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos
# saltos. O programa deve ser encerrado quando não for informado o nome do
# atleta. A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo
 
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

while True:
  saltos = []

  nome = input('Insira o nome do atleta: ')
  if nome == '':
    break
  else:
    for i in range(5):
      distancias = float(input('Insira a distância do {}° salto: '.format(i+1)))
      saltos.append(distancias)

    print('\nPrimeiro salto: {}'.format(saltos[0]),'m')
    print('Segundo salto: {}'.format(saltos[1]),'m')
    print('Terceiro salto: {}'.format(saltos[2]),'m')
    print('Quarto salto: {}'.format(saltos[3]),'m')
    print('Quinto salto: {}'.format(saltos[4]),'m')

    print('\nResultado Final:')
    print('Atleta: {}'.format(nome))

    somaSaltos = 0
    print('Saltos: ',end='')
    for i in range(len(saltos)):
      if i < len(saltos) - 1:
        print(saltos[i],'- ',end='')
      else:
        print(saltos[i])
      somaSaltos += saltos[i]

    media = somaSaltos / len(saltos)
    print('Média dos saltos: {}m'.format(media))
    print()
print('Fim do programa')
