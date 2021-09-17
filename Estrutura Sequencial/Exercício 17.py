# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro 
# para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
 
mts = float(input('Quantos m² tem a área a ser pintada: '))

# Litros de tinta necessários para a pintura
ltsNecess = mts / 3

# Quantidade de litros
lata = 18
galao = 3.6

# Preço
precoLata = 80
precoGalao = 25

print('Será necessário %.2f lts de tinta para realizar a pintura'%(ltsNecess))
print()

# Caso a quantidade de tinta não dê um valor exato do produto, será considerado uma lata a mais por excedente
excessoLata = 0
excessoGalao = 0
excesso10 = 0 # Tem a mesma função, porém é para a parte do código que considera latas e galões em conjunto

# Considerando somente latas de 18lts
qntLatas = ltsNecess // lata

# Realiza o módulo, para verificar se tem tinta ainda a ser considerada, e considera 1 unidade a mais caso verdadeiro
sobraLata = ltsNecess % lata
if sobraLata > 0:
      excessoLata = 1

print('Cosiderando latas de 18lts:')
print('Será necessário %i lata(s)'%(qntLatas + excessoLata))
print('Cada lata custa R$%u então a conta ficou em R$%.2f'%(precoLata,(qntLatas + excessoLata) * precoLata))
print()

# Considerando somente galao de 3.6lts
qntGalao = ltsNecess // galao

# Realiza o módulo, para verificar se tem tinta ainda a ser considerada, e considera 1 unidade a mais caso verdadeiro
sobraGalao = ltsNecess % galao
if sobraGalao > 0:
    excessoGalao = 1

print('Considerando galões de 3.6lts:')
print('Será necessário %i galão(ões)'%(qntGalao + excessoGalao))
print('Cada galão custa R$%i então a conta ficou em R$%.2f'%(precoGalao,(qntGalao + excessoGalao)*precoGalao))
print()


# Considerando latas e galões e com um excedente de 10% de tinta
tintaMais10 = (ltsNecess * 0.10) + ltsNecess

print('Considerando latas de 18lts e galões de 3.6lts juntos e uma sobra de 10% de tinta: ')
print('A quantidade de tinta necessária é de %.2flts'%(tintaMais10))
print()

qntLata10 = tintaMais10 // lata
sobraLata10 = tintaMais10 % lata

qntGalao10 = sobraLata // galao

# Realiza o módulo, para verificar se tem tinta ainda a ser considerada, e considera 1 unidade a mais caso verdadeiro
sobraGalao10 = qntGalao10 % galao
if sobraGalao > 0:
    excesso10 = 1

print('Será necessário %i latas de 18lts e %i galão(ões) de 3.6lts'%(qntLata10, qntGalao10 + excesso10))
print('A conta ficou em R$%.2f'%((qntLata10 * precoLata) + ((qntGalao10 + excesso10) * precoGalao)))