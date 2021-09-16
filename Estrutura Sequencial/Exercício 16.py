# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
# para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e
# o preço total.

mts = float(input('Quantos m² tem a área a ser pintada: '))
ltsNecess = mts / 3
lata = 18
precoLata = 80
excesso = 0

print('Será necessário %.2f litros de tinta.'%(ltsNecess))

qntLatas = ltsNecess // lata

sobra = ltsNecess % lata

if sobra > 0:
  excesso = 1

print('Será necessário %i lata(s) de 18lts'%(qntLatas + excesso))
print('Cada lata custa R$80 então a conta ficou em R$%.2f'%((qntLatas + excesso) * precoLata))
