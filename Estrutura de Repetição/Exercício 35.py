# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes
# entre 1 e um número inteiro informado pelo usuário.

# Lista que vai ser criada com os números primos
listaPrimos = []
# Variável de controle do laço while
testes = 0

x = int(input('Insira o valor a ser testado: '))
# Variável que vai decrementando nos cálculos
y = x 

while testes < x:
  # Lista para calcular se o número atual é primo
  lista = []
  contador = 0

  # Este laço a seguir pode ser mudado para que se ganhe performance nos cálculos
  for i in range(y,0,-1):
    lista.append(i)
    if y % i == 0:
      contador += 1
  
  # Caso só haja divisão por 1 e por ele mesmo, então é primo
  if contador == 2:
    listaPrimos.append(y)

  testes += 1
  y -= 1

print('Existem os seguintes primos até o número inserido: ',end='')
listaOrdenada = sorted(listaPrimos)

for i in range(len(listaOrdenada)):
  if i == len(listaOrdenada) -1:
    print(listaOrdenada[i],'.',end='')
  else:
    print(listaOrdenada[i],',',end='')
  
