# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.


# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.


valorHora = float(input('Quanto você ganha por hora? '))
horasMes = float(input('Quantas horas foram trabalhadas no mês? '))

salBruto = valorHora * horasMes
impostoRenda = 0.11 * salBruto
inss = 0.08 * salBruto
sindi = 0.05 * salBruto
salLiquido = salBruto - impostoRenda - inss - sindi

print('-'*30)
print('+ Salário Bruto: R$ %.2f'%(salBruto))
print('- Imposto de renda: R$ %.2f'%(impostoRenda))
print('- INSS: R$ %.2f'%(inss))
print('- Sindicato: R$ %.2f'%(sindi))
print('= Salário Líquido: R$ %.2f'%(salLiquido))
print('-'*30)





