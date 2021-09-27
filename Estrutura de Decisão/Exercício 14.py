# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição
# de conceitos obedece à tabela abaixo:
#    Média de Aproveitamento  Conceito
#    Entre 9.0 e 10.0        A
#    Entre 7.5 e 9.0         B
#    Entre 6.0 e 7.5         C
#    Entre 4.0 e 6.0         D
#    Entre 4.0 e zero        E
#    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” 
#    se o conceito for D ou E.

nota1 = float(input('Insira a primeira nota: '))

# Validação da nota 1
while nota1 < 0 or nota1 > 10:
  print('Verifique o valor inserido: ')
  nota1 = float(input('Insira a primeira nota: '))


nota2 = float(input('Insira a segunda nota: '))

# Validação da nota 2
while nota2 < 0 or nota2 > 10:
  print('Verifique o valor inserido: ')
  nota2 = float(input('Insira a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 9:
  conceito = 'A'
elif media >= 7.5:
  conceito = 'B'
elif media >= 6:
  conceito = 'C'
elif media >= 4:
  conceito = 'D'
elif media >= 0:
  conceito = 'E'
print('Sua média é %.2f que tem conceito %s'%(media,conceito))
