# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão\n')
op = int(input('Qual operação deseja realizar? '))

num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))

if op == 1:
  res = num1 + num2
elif op == 2:
  res = num1 - num2
elif op == 3:
  res = num1 * num2
elif op == 4:
  res = num1 / num2
else:
  print('Erro')

# Verifica se é ímpar ou par
if res % 2 == 0:
  resultadoE = 'par'
else:
  resultadoE = 'ímpar'
  

# Verifica se é par ou ímpar
if res > 0:
  resultadoPos = 'positivo'
elif res < 0:
  resultadoPos = 'negativo'
else:
  resultadoPos = 'neutro'

# Verifica se o número é indeiro ou decimal
arr = round(res,0) 

if arr == res:
  resInteiro = 'inteiro'
else:
  resInteiro = 'decimal'

print()
print('O resultado da operação é %.2f'%(res))
print('Este número é %s'%(resultadoE))
print('O número é %s'%(resultadoPos))
print('O número é um número %s'%(resInteiro))
