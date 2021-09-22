# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#    A mensagem "Reprovado", se a média for menor do que sete;
#    A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Insira a primeira nota parcial: '))
nota2 = float(input('Insira a segunda nota parcial: '))

media = (nota1 + nota2) / 2

if media == 10:
  print('Aprovado com distinção, Nota 10!')
elif media >= 7:
  print('Aprovado com média %i'%(media))
else:
  print('Reprovado com média %i'%(media))

