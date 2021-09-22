# Faça um Programa que leia três números e mostre o maior e o menor deles.

x = float(input('Insira o primeiro número: '))
y = float(input('Insira o segundo número: '))
z = float(input('Insira o terceiro número: '))
print()

# Lógica do maior número
if x > y and x > z:
  print('O maior número é :',x)
if y > x and y > z:
  print('O maior número é :',y)
if z > x and z > y:
  print('O maior número é :',z)

# Caso tenham 2 números repetidos e sejam os maiores
if x == y and x > z:
  print('Os maior número é o %.2f e ele aparece 2 vezes!'%(x))
if x == z and x > y:
  print('Os maior número é o %.2f e ele aparece 2 vezes!'%(x))
if y == z and y > x:
  print('Os maior número é o %.2f e ele aparece 2 vezes!'%(y))



# Lógica do menor número
if x < y and x < z:
  print('O menor número é :',x)
if y < x and y < z:
  print('O menor número é :',y)
if z < x and z < y:
  print('O menor número é :',z)

# Caso tenham 2 números repetidos e sejam os menores
if x == y and x < z:
  print('Os menor número é o %.2f e ele aparece 2 vezes!'%(x))
if x == z and x < y:
  print('Os menor número é o %.2f e ele aparece 2 vezes!'%(x))
if y == z and y < x:
  print('Os menor número é o %.2f e ele aparece 2 vezes!'%(y))


# Caso os três números inseridos sejam iguais
if x == y and y == z:
  print('Os três números inseridos são iguais!')
