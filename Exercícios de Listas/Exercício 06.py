# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num
# vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

# Esta função gera o nome da 'chave' número do Aluno 
# Ex: Aluno1, Aluno2...
def nomeVariavel(x):
  x = 'Aluno'+str(x +1)
  return(x)

dicionario = {}

# Primeiro laço é a quantidade de alunos
for i in range(10):   
  chave = nomeVariavel(i)
  
  # Segundo laço é a quantidade de notas por aluno
  total = 0 # Somatória das notas
  for j in range(4):
    nota = float(input('Insira a %i° nota do Aluno %i: '%(j+1,i+1))) 
    total = total + nota

  media = total / 4 # Quantidade de notas
  # Adiciona aluno e nota ao dicionário
  dicionario.update({chave:media}) 

alunosMedia = 0
print('\nAlunos acima da média: ')
for i,j in dicionario.items():
  if(j > 70):
    print('{} = {}'.format(i,j))
    alunosMedia += 1
print('Quantidade de alunos acima da média: %i'%(alunosMedia))
