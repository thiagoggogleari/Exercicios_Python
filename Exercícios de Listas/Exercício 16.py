# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus
# vendedores com base em comissões. O vendedor recebe $200 por semana 
# mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor
# que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de
# $3000, ou seja, um total de $470. Escreva um programa (usando um array de
# contadores) que determine quantos vendedores receberam salários nos seguintes
# intervalos de valores:

# $200 - $299 1°
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante 9°
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário,
# sem fazer vários ifs aninhados.

# As informações sobre salários não foram apresentadas, serão consideradas as seguintes
salarios = [250,250,300,350,280,450,800,800,1100,350]

ranges = [0,0,0,0,0,0,0,0,0]

j = 0

for i in range(len(salarios)):
  if salarios[i] > 200 and salarios[i] < 299:
    ranges[j] = ranges[j] + 1 
  elif salarios[i] > 300 and salarios[i] < 399:
    ranges[j+1] = ranges[j+1] + 1
  elif salarios[i] > 400 and salarios[i] < 499:
    ranges[j+2] = ranges[j+2] + 1
  elif salarios[i] > 500 and salarios[i] < 599:
    ranges[j+3] = ranges[j+3] + 1
  elif salarios[i] > 600 and salarios[i] < 699:
    ranges[j+4] = ranges[j+4] + 1
  elif salarios[i] > 700 and salarios[i] < 799:
    ranges[j+5] = ranges[j+5] + 1
  elif salarios[i] > 800 and salarios[i] < 899:
    ranges[j+6] = ranges[j+6] + 1
  elif salarios[i] > 900 and salarios[i] < 999:
    ranges[j+7] = ranges[j+6] + 1
  elif salarios[i] > 1000: 
    ranges[j+8] = ranges[j+8] + 1

# print(ranges)

# Gera tabela com os ranges possíveis

tabela = [200,299,300,399,400,499,500,599,600,699,700,799,800,899,900,999]

print('RANGE            QNTD')
j = 0
for i in range(8):
  print('Range',tabela[j],'-',tabela[j+1],': ',end='')
  print(ranges[i])
  j += 2
print('Range: acima10: ',ranges[i+1],end='')
