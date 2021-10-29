# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1

print("-== Verifica se é primo ==-")

while True:
  try:
    x = int(input('Digite um número (inteiro): '))
  except:
    print('É necessário um número inteiro como entrada.')
    continue
  else:
    break

numeros = x - 1 
contador = 0

while numeros > 1:
  # print(numeros)

  if (x % numeros) == 0:
    print('É divisivel por %i'%(numeros))
    contador += 1
 
  numeros -= 1
  
if contador == 0:
  print('O número %i é primo!'%(x))
else:
  print('O número %i não é primo'%(x))
