# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia
# o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

precoGasolina = 2.5
precoAlcool = 1.90

print('A = Álcool / G = Gasolina')
tipo = input('Qual o tipo de combustível? [A/G]')

while tipo.upper() not in ('A','G'):
  tipo = input('Qual o tipo de combustível? [A/G]')

litros = float(input('Quantos litros foram abastecidos?'))


if(tipo.upper() == 'A'):
  if(litros < 30):
    print('A conta ficou em: R$%.2f'%((precoAlcool - precoAlcool * 0.3) * litros))
  else:
     print('A conta ficou em: R$%.2f'%((precoAlcool - precoAlcool * 0.5) * litros))

if(tipo.upper() == 'G'):
  if(litros < 30):
    print('A conta ficou em: R$%.2f'%((precoGasolina - precoGasolina * 0.4) * litros))
  else:
    print('A conta ficou em: R$%.2f'%((precoGasolina - precoGasolina * 0.6) * litros))
