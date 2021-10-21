# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

base = int(input('Insira o número da base: '))
expoente = int(input('Insira o número do expoente: '))

# -- Propriedade da exponenciação --
# Caso expoente seja 0 o resultado é igual a 1
if expoente == 0:
  calculo = 1

# -- Propriedade da exponenciação --
# Caso expoente seja 1 o resultado é igual a base
elif expoente == 1:
  calculo = base

else:
   # -- Propriedade da exponenciação --
  # Caso base e expoente sejam negativos, é invertido o sinal de ambos para 
  # primeira parte do cálculo, e adicionado uma flag para que se entre em outro
  # laço com a expressão para resolução desta propriedade
  flag = 0
   
  if base < 0 and expoente < 0:
    base = base * (-1)
    expoente = expoente * (-1)
    flag = 1

  # Realiza o primeiro calculo
  calculo = base * base
   
  # Contador começa em 2, pois considera -1 da primeira operação(calculo)
  contador = 2

  while  contador < expoente:
    calculo = calculo * base
    contador += 1

# Se a base for positiva e o expoente for ímpar o resultado é negativado. 
if expoente % 2 != 0 and (expoente < 0 and base > 0):
  calculo = calculo * -1

# Se base e expoente são negativos -a ^-n = 1 / - (a * a *...n vezes)
if flag == 1:
  calculo = 1 / ((-1) *calculo)

print('O resultado da operação é: {}'.format(calculo))
