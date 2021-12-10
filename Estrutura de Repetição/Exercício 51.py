# Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
# Imprima no final a soma da série.

dividendo = 1
divisor = 1
somatoria = 0

n = int(input('Quantos termos deseja calcular?'))

print('S = ',end='')

for i in range(n):  
  # Caso não seja o último cálculo, adiciona o sinal de '+' ao final da string.
  if i < n-1:
    print('%i/%i +'%(dividendo,divisor),end='')
    somatoria = somatoria + (dividendo / divisor)
    dividendo += 1
    divisor += 2
  else:
    print('%i/%i.'%(dividendo,divisor))
    somatoria = somatoria + (dividendo / divisor)

print('\nA somatória do resultados dos termos é de ~%.2f.'%(somatoria))
