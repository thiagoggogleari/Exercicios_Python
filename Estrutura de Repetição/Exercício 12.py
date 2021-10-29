# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

print('*** Gerador de Tabuada ***')
num = int(input('Insira um número: '))

while num < 1 or num > 10:
  print('O número deve estar entre 1 e 10')
  num = int(input('Insira um número inteiro entre 1 e 10: '))

for i  in range(11):
  print('%i x %i = %i'%(num,i, i * num))
  i += 1
