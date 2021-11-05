# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. 
# A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

entrada = int(input('Insira um número que deseja saber o fatorial: '))

# Valida entrada
while entrada < 0:
  print('Não existe fatorial de número negativo!')
  entrada = int(input('Insira um número que deseja saber o fatorial: '))

conta = entrada
anterior = entrada - 1

# Primeiro trecho da frase 
print('%i! = '%(entrada),end='')

# Propriedade do fatorial
if entrada == 0 or entrada == 1:
  print('1')
else:
  print('%i . '%(entrada),end='')
  while anterior > 0:
    if anterior != 1:
      print(anterior,'. ',end='')
    # Caso seja o último dígito, finaliza com '='
    else:
      print(anterior,'= ',end='')
    conta = conta * anterior # Calculo do fatorial (a cada passada no laço)
    anterior -= 1 
  # Imprime o resultado no final
  print(conta)
