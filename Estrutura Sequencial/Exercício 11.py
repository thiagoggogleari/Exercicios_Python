
# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.


i1 = int(input('Insira um número inteiro: '))
i2 = int(input('Insira outro número inteiro: '))
r1 = float(input('Insira um número Real: '))

print('O produto do dobro de %i com a metade de %i é: %i.'%(i1, i2, (i1 * 2) * (i2 / 2)))
print('A soma do triplo de %i com %.2f é: %.2f'%(i1, r1, (3 * i1) + r1))
print('O número %.2f elevado ao cubo(³) é: %.2f'%(r1, r1**3))

