# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados. 


while True:
  try:
    entrada = int(input('Insira um número :'))
  except:
    print('É necessário que o número seja do tipo inteiro!')
    continue
  else:
    break

multiplos = 0
contador = entrada
calculos = 0
flag = 1 # Sinaliza para decrementar de 1 em 1


if entrada % 2 == 0: # *1 - calculo de divisão
  flag = 0 # indica que o número é par, para que se decremente de 2 em 2,feito isto considerando pares > 2 como não primos

while contador > 0:
  # print(contador)
  # A cada passada no laço, é realizado um cálculo de divisão no 'if'
  calculos += 1
  if entrada % contador == 0: 
    print('É divisível por %i.'%(contador))
    multiplos += 1

  if flag == 1:
    contador -= 2
  else:
    contador -= 1
    flag = 1

print()
if entrada == 1 or entrada < 0:
  print('O número %i por definição não é considerado um número primo.'%(entrada))
elif multiplos == 2:
  print('O número %i é divisível somente por 1 e por ele mesmo, portanto ele é primo!'%(entrada))
else:
  print('O número %i é divisível por %i número(s), além de 1 e dele mesmo. Portanto ele não é primo'%(entrada,multiplos -2))
  print()
  print('Foram executadas %i operações com divisão neste programa'%(calculos))
