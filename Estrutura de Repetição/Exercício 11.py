# Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Insira um número inteiro: '))
num2 = int(input('Insira outro número inteiro: '))
print()

soma = 0

# Caso o segundo número seja maior
if num2 > num1: 
  
  # Diferença entre os números inseridos
  rangeEntreNum = num2 - num13

  # Caso os números seja sequenciais, não há inteiro entre eles
  if rangeEntreNum == 1:
    print('Não há números inteiros entre os números inseridos')
    soma = num1 + num2
  else:
    print('Os números inteiros entre os números inseridos são: ')
    print('Z = ',end='')

  # Faz um laço para repetir os números com base no tamanho da diferença
  # entre os números inseridos 

  for i in range(rangeEntreNum -1):
    # Vai incrementando o menor número inserido de 1 em 1 a cada repetição
    num1 += 1
    soma = soma + num1
    
    # Caso seja a última posição, o último print é realizado com um '.'
    # Caso contrário é inserido uma ',' entre os dígitos

    if i == rangeEntreNum -2:
      print(num1,'. ')
    else:
      print(num1,', ',end='')
    
 
  print('A soma dos números é %i.'%(soma))
  
# Este bloco tem a mesma lógica que o bloco acima
elif num1 > num2:
  rangeEntreNum = num1 - num2
    
  if rangeEntreNum == 1:
    print('Não há números inteiros entre os números inseridos')
    soma = num1 + num2
  else:
    print('Os números inteiros entre os números inseridos são: ')
    print('Z = ',end='')

  for i in range(rangeEntreNum -1):
    num2 += 1
    soma = soma + num2

    if i == rangeEntreNum -2:
      print(num2,'. ')
    else:
      print(num2,', ',end='')
    
  print('A soma dos números é %i.'%(soma))

else:
  # Caso não atenda as condições acima, então os números são iguais
  print('Os números inseridos são iguais.')
