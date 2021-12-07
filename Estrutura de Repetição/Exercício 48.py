# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.

# Exemplo:
# 12376489
# => 98467321

while True:
  try:
    num = int(input('Insira o número inteiro e positivo:'))
    
    if num > 0:
      break

  except:
    print('O número precisa ser positivo e inteiro\n')
    continue

print()
numStr = str(num)
tam = len(numStr)

for i in range(tam,0,-1):
  print(numStr[i -1],end='')
