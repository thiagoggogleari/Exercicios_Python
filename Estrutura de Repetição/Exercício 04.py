# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%e que a população
# e B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários
# para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

# Habitantes
paisA = 8000
taxaCrescA = 0.03

paisB = 200000
taxaCrescB = 0.015

contador = 0
ano = 0

while paisB > paisA:
  ano += 1
  paisA = paisA + (paisA * taxaCrescA)
  paisB = paisB + (paisB * taxaCrescB)

print('O país B irá ultrapassar o país A no %i° ano'%(ano))
print()
print('País A = %i habitantes'%(paisA))
print('País B = %i habitantes'%(paisB))
