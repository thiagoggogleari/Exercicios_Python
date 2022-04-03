# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. 
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo 
# igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para 
# valores dentro da faixa de forma elegante.

def desenhaRetangulo(qntdLinhas, qntdColunas):
  print('+', '-' * qntdColunas, '+')

  for i in range(qntdLinhas):
    print('|', ' ' * qntdColunas, '|')

  print('+', '-' * qntdColunas, '+')


entradaLinhas = int(input("Insira o número de linhas: "))
if (entradaLinhas < 1):
  entradaLinhas = 1

entradaColunas = int(input("Insira o número de colunas: "))
if (entradaColunas > 20):
  entradaColunas = 20

desenhaRetangulo(entradaLinhas, entradaColunas)
