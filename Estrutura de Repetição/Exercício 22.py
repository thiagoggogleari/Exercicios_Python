# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

# Este é o mesmo código que o do exercício 21, pois eu já havia implantado esta nova rotina.

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
