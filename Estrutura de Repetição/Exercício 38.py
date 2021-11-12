# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo
# que o usuário digite o salário inicial do funcionário.

salario = float(input('Qual o salário inicial do funcionário: '))
porcentual = 0.015 #1.5%
ano = 1996

for i in range(6):
  print('-'*30)
  print('Ano: ',ano)
  print('Salário anterior: R$ %.2f'%(salario))
  
  aumento = salario * porcentual
  print('Aumento: {:.2f}%'.format(aumento /100))
  
  salarioDoAno =  salario + aumento 
  print('Salário: R$ %.2f'%(salarioDoAno))
  
  ano += 1
  salario = salarioDoAno
  porcentual = porcentual * 2

  print('-'*30,'\n')
