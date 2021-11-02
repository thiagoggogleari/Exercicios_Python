# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de 
# turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos. 

turmas = int(input('Qual a quantidade de turmas? '))
while turmas > 40 and turmas < 1:
  print('Quantidade máxima de turmas é 40!')
  turmas = int(input('Qual a quantidade de turmas? '))

totalAlunos = 0

for i in range(turmas):
  alunoTurma = int(input('Quantos alunos tem na turma %i? '%(i + 1)))
  totalAlunos = totalAlunos + alunoTurma

print('A quantidade média de alunos por turma é de aproximadamente %i alunos.'%(round(totalAlunos / turmas,0)))
