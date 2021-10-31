# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se
# a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é
# jovem, adulta ou idosa, conforme a média calculada

pessoas = int(input('Quantas pessoas irão fazer parte da pesquisa? '))
totalIdade = 0

for i in range(pessoas):
  idade = int(input('Qual a idade da %i pessoa? '%(i + 1)))
  totalIdade = totalIdade + idade

media = totalIdade / pessoas
print('A média de idade das pessoas é de %.2f anos.'%(media))

if media > 0 and media <= 25:
  print('A média de idade da turma está relacionada a idade Jovem.')
elif media > 25 and media <= 60:
  print('A média de idade da turma está relacionada a idade Adulta')
elif media > 60 and media < 150:
  print('A média de idade da turma está relacionada a idade Idosa')
else:
  print('Verifique os valores e tente novamente')
