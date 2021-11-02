# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
# e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

cds = int(input('Quantos cd´s possui em sua coleção? '))
totalInvestido = 0


for i in range(cds):
  preco = float(input('Qual o preço do cd %i? '%(i + 1)))
  totalInvestido = totalInvestido + preco

print('O total investido na coleção é de R$%.2f'%(totalInvestido))
print('A média de preço por cd´s é de R$%.2f'%(totalInvestido / cds))
