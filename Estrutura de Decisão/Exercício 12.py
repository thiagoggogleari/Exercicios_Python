# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme
#   tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário 
#    Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# 
#    Desconto do IR:
#    Salário Bruto até 900 (inclusive) - isento
#    Salário Bruto até 1500 (inclusive) - desconto de 5%
#    Salário Bruto até 2500 (inclusive) - desconto de 10%
#    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e
#    a quantidade de hora é 220.
#            Salário Bruto: (5 * 220)        : R$ 1100,00
#            (-) IR (5%)                     : R$   55,00  
#            (-) INSS ( 10%)                 : R$  110,00
#            FGTS (11%)                      : R$  121,00
#            Total de descontos              : R$  165,00
#            Salário Liquido                 : R$  935,00


# No código de exemplo fornecido acima não está sendo considerado o desconto do sindicato

valorHora = float(input('Qual o valor da hora? '))
horasTrab = float(input('Quantas horas foram trabalhadas no mês? '))

salBruto = valorHora * horasTrab

perInss = 0.10
inss = salBruto * perInss

# Sindicato 3%
perSindicato = 0.03
sindicato = salBruto * perSindicato

# Fgts não é descontado do funcionário
perFgts = 0.11
fgts = salBruto * perFgts


if salBruto <= 900:
  perIrenda = 0
elif salBruto <= 1500:
  perIrenda = 0.05
elif salBruto <= 2500:
  perIrenda = 0.1
elif salBruto > 2500:
  perIrenda = 0.2

iRenda = salBruto * perIrenda 
print()

# Espaçamento entre descrição e valor
spaces = 35

# Primera parte da string
string1 = ('Salário Bruto: ({}*{})'.format(valorHora,horasTrab))
print(string1,end='')

# Espaçamento
print('-'*(spaces - len(string1)),end='')

# Segunda parte da string
print(': R${:.2f}'.format(salBruto))


string2 = ('(-) IR ({}%)'.format(perIrenda * 100))
print(string2,end='')
print('-'*(spaces - len(string2)),end='')
print(': R${:.2f}'.format(iRenda))

string3 = ('(-) INSS ({:.2f}%)'.format(perInss * 100))
print(string3,end='')
print('-'*(spaces - len(string3)),end='')
print(': R${:.2f}'.format(inss))

string4 = ('(-) FGTS ({:.2f}%)'.format(perFgts* 100))
print(string4,end='')
print('-'*(spaces - len(string4)),end='')
print(': R${:.2f}'.format(fgts)) # Não é descontado

string5 = ('(-) SINDICATO ({:.2f}%)'.format(perSindicato * 100))
print(string5,end='')
print('-'*(spaces - len(string5)),end='')
print(': R${:.2f}'.format(sindicato))
print()

string6 = ('Total de descontos:')
print(string6,end='')
print('-'*(spaces - len(string6)),end='')
print(': R${:.2f}'.format(salBruto - iRenda - inss - sindicato))