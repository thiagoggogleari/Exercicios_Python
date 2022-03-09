# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados,
# obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" 
# e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é 
# continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 
# antes de tirar este Ponto novamente.

import random

def jogadados():
  return random.randint(2,12)

marcadorPonto = 0

while True:
  txt = input("Digite ENTER para lançar os dados ou qualquer outra tecla para sair")
  if(txt != ""): 
    break
  
  # Chama a função que gera o número aleatório
  jogada = jogadados();

  print('Primeiro lance de dados: {}'.format(jogada))
  print()

  # Verificações de acordo com a regra do jogo  
  if (jogada == 7 and marcadorPonto != 0):
    print('Você perdeu!')
    break

  if (jogada == 7 or jogada == 11):
    print('Natural, ganhou!')
    break

  elif(jogada == 2 or jogada == 3 or jogada == 12):
    print('CRAPS! Você perdeu!')
    break
  # Caso a tecla pressionada não seja o "ENTER", o jogo é finalizado
    
  else:
    print('Ponto\n')
    # Variável armazenada para comparação com as próximas jogadas
    marcadorPonto = jogada
    
    while True:
      txt = input("Digite ENTER para lançar os dados ou qualquer outra tecla para sair")
      if txt != "":
        break
      
      novaJogada = jogadados();
      
      if (novaJogada == 7):
        print('\nVocê tirou um 7 e perdeu!')
        break
      if (novaJogada == marcadorPonto):
        print('\nVocê tirou o mesmo número! ({}) '.format(marcadorPonto))
        break
      else:
        print('Nova jogada = {}'.format(novaJogada))

    # Finaliza o primeiro while
    break  

print('\nFim de jogo!')
