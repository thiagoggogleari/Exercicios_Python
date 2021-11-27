# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
# o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar
# com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto
# por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se 
# outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.

# Gabarito da Prova:
# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A

listaRespostaProva = ['A','B','C','D','E','E','D','C','B','A']
listaTodasNotas = []

while True: 
  listaRespostaAluno = []
  acertos = 0
  questoes = 10 # Altera a quantidade de questões

  # Coleta as respostas e vai adicionando à lista
  for i in range(questoes):
    entrada = input('Insira a resposta da %i pergunta: '%(i+1))
    listaRespostaAluno.append(entrada.upper())

  # Compara as duas listas(Gabarito e respostas dos alunos)
  for i in range(questoes):
    if listaRespostaAluno[i] == listaRespostaProva[i]:
      acertos += 1

  print('Total de acertos: %i'%(acertos))
  print('Nota: %i'%(acertos))
  listaTodasNotas.append(acertos)
   
  perguntaAluno = input('\nOutro aluno irá utilizar o sistema? [S/N]')
  while perguntaAluno.upper() not in ('S','N'):
      perguntaAluno = input('\nOutro aluno irá utilizar o sistema? [S/N]')

  if perguntaAluno.upper() == 'N':
    break
  
  
# Realiza a soma de todas as notas para depois realizar o cálculo de média
totalNotas = 0
for i in range(len(listaTodasNotas)):
  totalNotas += listaTodasNotas[i]

# Organiza a lista para coletar a menor e maior nota
oListaTodasNotas = sorted(listaTodasNotas)
menor = oListaTodasNotas[0]
maior = oListaTodasNotas[len(oListaTodasNotas)-1]

print('\nA menor nota é de: %i'%(menor))
print('A maior nota é de: %i'%(maior))
print('Total de alunos que participaram: %i'%(len(listaTodasNotas)))
print('A média de todas as notas das turma é de: %.2f'%(totalNotas / len(listaTodasNotas)))
