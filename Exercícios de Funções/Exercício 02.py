# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n

# Inserir aqui a quantidade de operações desejadas
n = 10

def calcula(x):
  # Este contador é responsável pelo numero inicial das impressões
  contador = 0
  
  # Este contador é responsável pelo avanço do passo das imperssões
  contador1 = 1
  
  # Executa o loop 'n' vezes
  for i in range(x):
    # Imprime a quantidade máxima de acordo com contador 1
    while contador < contador1:
      print('{} '.format(contador + 1),end='')
      contador += 1
      
    print()
    # Reseta o número inicial
    contador = 0

    # Incrementa o passo em 1
    contador1 += 1 

# Executa a função
calcula(n)
