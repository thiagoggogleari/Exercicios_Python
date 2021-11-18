# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.#
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25

# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67


divida = float(input('Digite o valor da divida: '))

juros = [0,10,15,20,25]
parcelas = [1,3,6,9,12]

print('Valor da dívida   |   Valor dos juros  |   Parcelas   |  Valor da parcela')

for i in range(5):
############################################################################## 
  # Dívida
  valorDaDivida = round(divida + (juros[i] / 100) * divida,2)
  valorDaDividaFORMAT = len('%.2f'%(valorDaDivida))
  espacosDivida = 13 - valorDaDividaFORMAT

  print(' '*(espacosDivida),end='')
  print('R$%.2f'%(valorDaDivida),end='') # Fixo

##############################################################################
  # Valor dos juros
  valorDosJuros = round((juros[i] / 100)* divida,2)
  valorDosJurosFORMAT = len('%.2f'%(valorDosJuros))
  espacosJuros = 20 - valorDosJurosFORMAT

  print(' '*(espacosJuros),end='')
  print('R$%.2f'%(valorDosJuros),end='') 

##############################################################################
  # Parcelas
  espacosParcelas = 14 - len(str(parcelas[i]))

  print(' '*(espacosParcelas),end='')
  print(parcelas[i],end='')# Altera
##############################################################################
  # Valor das Parcelas
  valorDaParcela = round(valorDaDivida / parcelas[i], 2)  
  valorDaParcelaFORMAT = len('%2f'%(valorDaParcela))
  espacosValorDaParcela = 24 - valorDaParcelaFORMAT

  print(' '*(espacosValorDaParcela),end='')
  print('R$%.2f'%(valorDaParcela))
