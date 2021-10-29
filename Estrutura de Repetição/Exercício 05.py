
# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

while True:
  paisA = int(input('Insira a quantidade de habitantes do país A: ' ))
  taxaCrescA = float(input('Insira a taxa de crescimento (porcentagem) no país A:  '))
  taxaCrescA = taxaCrescA / 100
  
  # Valida dados país A
  if(paisA < 0 or taxaCrescA < 0 or taxaCrescA > 1):
    print('\nOs dados inseridos são inválidos \n')
    continue

  paisB = int(input('Insira a quantidade de habitantes do país B: '))
  taxaCrescB = float(input('Insira a taxa de crescimento (porcentagem) no país B: '))
  taxaCrescB = taxaCrescB / 100

  # Valida dados país B
  if(paisB < 0 or taxaCrescB < 0 or taxaCrescB > 100):
    print('\nOs dados inseridos são inválidos, programa reiniciado! \n')
    continue
  
  # Valida os parâmetros inseridos, para constatar a possibilidade do cálculo
  if(paisA > paisB):
    print('\nPaís A já possui mais habitantes do que o país B! \n')
    continue

  if (taxaCrescA == taxaCrescB):
    print('\nAs taxas de crescimento não podem ser iguais, programa reiniciado! \n')
    continue
  if (taxaCrescA < taxaCrescB):
    print('\nA taxa de crescimento do país A deve ser maior do que a do país B.')
    print('Programa reiniciado!\n')
    continue

  # Variável de contador para o laço while
  ano = 0
  
  while paisB > paisA:
    ano += 1
    paisA = paisA + (paisA * taxaCrescA)
    paisB = paisB + (paisB * taxaCrescB)

  print()
  print('-'*60)
  print('O país A irá ultrapassar o país B no %i° ano.'%(ano))
  print('País A = %i habitantes'%(paisA))
  print('País B = %i habitantes'%(paisB))
  print('\n **** Cálculo Finalizado ***')
  print('-'*60)
  print()
