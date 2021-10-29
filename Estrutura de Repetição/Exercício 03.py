# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input('Insira o nome: ')
while len(nome) < 4:
  nome = input('Insira o nome: ')

idade = int(input('Insira a idade: '))
while idade < 0 or idade > 150:
  idade = int(input('Insira a idade: '))

salario = float(input('Informe seu salário: '))
while salario < 0:
  salario = float(input('Informe seu salário: '))

sexo = input('Informe o sexo: [F / M]')
while sexo not in ('F','f','M','m'):
  sexo = input('Informe o sexo: [F / M]')

estCivil = input('Informe estado civil: [S/C/V/D]')
while estCivil.upper() not in ('S','C','V','D'):
  estCivil = input('Informe estado civil: [S/C/V/D]')
