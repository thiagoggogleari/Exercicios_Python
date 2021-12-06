# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
# A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos
# restantes. Você deve fazer um programa que receba o nome do ginasta e as notas
# dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe 
# a sua média, conforme a descrição acima informada (retirar o melhor e o pior 
# salto e depois calcular a média com as notas restantes). As notas não são informados 
# ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7

# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04

nome = input('Insira o nome do atleta: ')
notas = []

# Este laço vai adicionando à lista as notas
for i in range (7):
  notaAtleta = float(input('Insira a nota: '))
  notas.append(notaAtleta)

# Organiza a lista em ordem numérica. Apaga primeiro e último registro.
notasOrdenadas = sorted(notas)
del notasOrdenadas[len(notasOrdenadas)-1]
del notasOrdenadas[0]

# Calcula a média
calculo = 0
for i in range(len(notasOrdenadas)):
  calculo = calculo + notasOrdenadas[i]

media = calculo / (len(notasOrdenadas))

# Saída
print()
print('*'*30)
print('Resultado Final')
print('Atleta: %s'%(nome))
print('Melhor nota: %.2f'%(notasOrdenadas[len(notasOrdenadas)-1]))
print('Pior nota: %.2f'%(notasOrdenadas[0]))
print('Média: %.2f'%(media))
print('*'*30)
