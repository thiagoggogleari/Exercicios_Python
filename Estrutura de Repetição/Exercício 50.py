# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, 
# Faça um programa que calcule o valor de H com N termos.

h = int(input('Qual o valor para H: '))
n = int(input('Qual o valor para N: '))

contador = 2 # o primeiro dígito a ser feito a operação de divisão
somatoria = 0

print('\nH = %i + '%(h),end='')

for i in range(n -1):
 # Caso seja o último loop, passa para o else que não imprime o sinal de '+'
  if i < n-2:
    print('%i/%i + '%(h,contador),end='')
    somatoria = somatoria + (h/contador)
    contador += 1
  else:
    print('%i/%i.'%(h,contador))
    somatoria = somatoria +(h / contador)
    
print('O resultado final é de ~%.2f'%(somatoria))
