# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
# receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade
# de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de
# carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

print('1 - Filé Duplo')
print('2 - Alcatra')
print('3 - Picanha')

opcaoCarne = int(input('Qual tipo de carne você deseja? [1/2/3]'))
while opcaoCarne not in (1,2,3):
  opcaoCarne = int(input('Qual tipo de carne você deseja? [1/2/3]'))

qntKilos = float(input('Quantos kilos deseja? '))

opcaoCartao = input('Irá pagar com cartão tabajara? [S/N]')
while opcaoCartao not in ('S','s','N','n'):
  opcaoCartao = input('Irá pagar com cartão tabajara? [S/N]')


print()
# Preço dos produtos

# Até 5 kg
fileDuplo = 4.90
alcatra = 5.90
picanha = 6.90

# Acima de 5 kg
acimaFileDuplo = 5.80
acimaAlcatra = 6.80
acimaPicanha = 7.80

# Desconto cartão tabajara
# Sobre o total
descontoCartao = 0.05

if(opcaoCarne == 1):
  carne = 'Filé Duplo'
  if qntKilos <= 5:    
    precoTotalCarne = qntKilos * fileDuplo
  else:
    precoTotalCarne = qntKilos * acimaFileDuplo

if(opcaoCarne == 2):
  carne = 'Alcatra'
  if qntKilos <= 5:
    precoTotalCarne = qntKilos * alcatra
  else:
    precoTotalCarne = qntKilos * acimaAlcatra

if(opcaoCarne == 3):
  carne = 'Picanha'
  if qntKilos <= 5:
    precoTotalCarne = qntKilos * picanha
  else:
    precoTotalCarne = qntKilos * acimaPicanha

# Caso o pagamento seja realizado no cartão Tabajara, é aplicado o desconto
if(opcaoCartao in ('S','s')):
  precoFinal = precoTotalCarne - (precoTotalCarne * descontoCartao)
else:
  precoFinal = precoTotalCarne
 

# Cupom Fiscal
print('*'*42)
print('-------------- Cupom Fiscal --------------\n')

print('Produto:            %s'%(carne))
print('Quantidade:         %.2f kg'%(qntKilos))
print('Preço total:        R$%.2f'%(precoTotalCarne))

if(opcaoCartao in ('S','s')):
  print()
  print('Desconto de 5% compra no cartão Tabajara')
  print('Valor do desconto: R${:.2f}'.format(precoTotalCarne * descontoCartao))
else:
  print('Cliente não teve desconto do cartão TABAJARA')

print()
print('Preço Final R$%.2f'%(precoFinal))

print('-'*42)
print('*'*42)


