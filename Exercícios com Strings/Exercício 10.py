# 10 Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
# Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de 
# "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando
# os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

# Foi criado uma rotina automática para geração de números para facilitar a demonstração do funcionamento do programa

import random

# Função que gera um número aleatório de 2 à 12
def rolarDado():
  dado = random.randint(2,12)  
  print("O dado deu: %i"%(dado))
  return dado

dado = rolarDado()

if(dado in (7,11)):
  print("Você tirou %i na primeira jogada!"%(dado))
  print("Você é um natural e ganhou!")
  
if(dado in (2,3,12)):
  print("Você tirou %i na primeira jogada!"%(dado))
  print("Craps. Você perdeu!")

if(dado in (4,5,6,8,9,10)):
  ponto = dado;
  print("\nVocê tirou %i e este é o seu \"PONTO\""%(ponto))
  print("Tire novamente este número para vencer!\n")


valorDado = 0

while True:
  # A cada nova passada pelo laço, um novo número é gerado
  valorDado = rolarDado()

  if(valorDado == ponto):
    print("Você tirou %i novamente! Venceu!"%(valorDado))
    print("Você Venceu!")    
    break
  elif(valorDado == 7):
    print("Você tirou 7.")
    print("Você Perdeu!")
    break
