# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

kgMorango = float(input('Quantos kg de Morango foram comprados? '))
kgMaca =float(input('Quantos kg de Maçã foram comprado? '))

# Até 5kg
precoMorango = 2.50
precoMaca = 1.80

# Acima de 5kg
precoMorangoDesc = 2.20
precoMacaDesc = 2.50

# Realiza o cálculo de preço da compra
if kgMorango < 5:
  totalMorango = precoMorango * kgMorango
else:
  totalMorango = precoMorangoDesc * kgMorango

if kgMaca < 5:
  totalMaca = precoMaca * kgMaca
else:
  totalMaca = precoMacaDesc * kgMaca

# Caso compre acima de 8 kg ou a conta dê acima de 25 reais, aplica desconto de 10%
if kgMorango + kgMaca > 8 or (totalMorango + totalMaca) > 25:
  desconto =(totalMorango + totalMaca) * 0.1
  total = (totalMorango + totalMaca) - desconto
  print('Recebeu um desconto de 10%')
else:
  total = totalMorango + totalMaca

print('A conta ficou em R$%.2f.'%(total))
