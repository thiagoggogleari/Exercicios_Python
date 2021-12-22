# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média
# anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
temperaturas = []

# Adiciona as temperaturas à lista
for i in range(12):
  entrada = float(input('Insira a média de temperatura (°C) do mês de %s: '%(meses[i])))
  temperaturas.append(entrada)

# Calculo da média
totalTemperaturas = 0

for i in range(12):
  totalTemperaturas = totalTemperaturas + temperaturas[i]

media = round((totalTemperaturas / 12), 2)

print('\nA média anual é de %.2f°C'%(media))

# Resultado
print('\nOs meses com temperatura acima da média anual são:')
for i in range(12):
  if temperaturas[i] > media:
    print('Mês %i - %s = %.1f°C'%(i+1, meses[i], temperaturas[i]))
