# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = float(input('Qual a altura da pessoa? '))

idealHomem = (72.7 * h) - 58
idealMulher = (62.1 * h) - 44.7

print('Para a altura informada o peso ideal para um Homem é de %.2fkg e para uma Mulher é de %.2fkg'%(idealHomem,idealMulher))