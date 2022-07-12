# 13 Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que 
# adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa 
# terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
# O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve 
# ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.


# -----------------------------------------------------------------------------------------------
# Este código é uma adaptação do código do exercício 11 aonde foi desenvolvido um jogo da velha.
# A diferença é que neste jogo, a palavra é embaralhada.
# -----------------------------------------------------------------------------------------------

# Comando para instalar a biblioteca unidecode no google colab
# !pip install unidecode

import random
import unidecode
import urllib3

# Local do arquivo aonde está armazenado a lista de palavras, neste código utilizo os nomes dos pokemons como palavras
url = 'http://raw.githubusercontent.com/thiagoggogleari/exercicios_python/main/Exerc%C3%ADcios%20com%20Strings/Lista_Exercicio_11.txt'
http = urllib3.PoolManager()
urllib3.disable_warnings()
response = http.request('GET',url)

arquivoCopia = (response.data).decode("utf-8") 
arquivoPokemon = arquivoCopia.split("\r\n")

print("-"*50)
print(" "*10,"Jogo da forca do Pokemon!")
print("São válidos os 151 pokemons da 1° temporada")
print("**NÍVEL DIFÍCIL, as letras estão embaralhadas!**");
print("Quem é esse pokemon?")
print("-"*50)


# Palavra a ser descoberta
#palavraDoSegredo = linhas[x].rstrip()
x = random.randint(0,150)

# Copia o nome de um pokemon
palavraDoSegredoOriginal = arquivoPokemon[x]

# Trata a palavra para embaralhá-la e a converte para maiúscula
palavraDoSegredo = sample(palavraDoSegredoOriginal,len(palavraDoSegredoOriginal))
palavraDoSegredo = ''.join(palavraDoSegredo)
palavraDoSegredo = palavraDoSegredo.upper()

def validaEntrada(entrada):
  while(len(entrada) > 1 or ((entrada.isalpha() == False))):
    print("--> Entrada inválida! Verifique e tente novamente <--")
    entrada = input("Letra: ")

# Monta o boneco de acordo com a quantidade de erros feitos
def boneco(erros):
  if(erros == 0):
    print("_____\n|\n|\n|\n|")
  elif(erros == 1):
    print("_____\n|   o\n|\n|\n|")
  elif(erros == 2):
    print("_____\n|   o\n|  /\n|\n|")
  elif(erros == 3):
    print("_____\n|   o\n|  /|\n|\n|")
  elif(erros == 4):
    print("_____\n|   o\n|  /|\\\n|\n|")
  elif(erros == 5):
    print("_____\n|   o\n|  /|\\\n|  /\n|")
  elif(erros == 6):
    print("_____\n|   o\n|  /|\\\n|  / \\\n|")
  elif(erros == 7):
    print("_____\n|   X\n|  /|\\\n|  / \\\n|")
  print()

def letrasJaInseridas():
  print("Letras já inseridas: ")
  for letras in range(len(letrasInseridas)):
    print(letrasInseridas[letras]," ",end="")
  print('\n')


# Esta lista é apresentada ao jogador durante o jogo e sendo atualizada durante
lista = []

# Monta os campos do jogo de acordo com o tamanho da palavra
boneco(0)
for l in range(len(palavraDoSegredo)):
  lista.append("_")
  print("_ ",end="")

entrada = input("\nInsira uma letra: ")
print("-"*50)
validaEntrada(entrada)

# Converte a letra de 'entrada' para maiúscula e sem acentos
letra = unidecode.unidecode(entrada.upper())

# Aqui é criado uma String com a 'palavraDoSegredo' sem acentos e em maiúsculo.
# É realizado a comparação entre a letra inserida e as letras desta variável.
# Quando o jogador acerta a letra, o programa preenche com o valor
# original da variável 'palavraDoSegredo'
segredo = unidecode.unidecode(palavraDoSegredo.upper())

# Armazena a quantidade de erros
tentativas = 0

# Lista aonde são armazenadas as letras jogadas
letrasInseridas = []

while True:
  contadorAcertoLetras = 0
  repetido = False

  # Faz uma varredura e verifica se a letra está presente na palavraDoSegredo
  for i in range(len(segredo)):
    if(letra == segredo[i]):
      lista[i] = palavraDoSegredo[i]
      contadorAcertoLetras += 1
  
  # Uma variável informa se a letra é repetida
  if((letra in letrasInseridas) == True):
    letrasJaInseridas()
    print("Esta letra já foi!")
    boneco(tentativas)
    repetido = True
  else:
    letrasInseridas.append(letra)
    repetido = False
  
  # Mostra a quantidade de letras que o jogador acertou ou a quantidade de erros
  if(contadorAcertoLetras > 0 and (repetido == False)):
    letrasJaInseridas()
    print("Você acertou %i letra(s)"%(contadorAcertoLetras))
    boneco(tentativas)
  elif(contadorAcertoLetras == 0 and (repetido == False)):
    tentativas += 1
    if (tentativas > 6):
      letrasJaInseridas()
      print("\n-> Você errou pela %i° vez!"%(tentativas))  
      boneco(tentativas)
      print("Fim de jogo. Você perdeu!")
      print("O pokemon desconhecido era:\n%s"%(palavraDoSegredoOriginal))
      print("-"*50)
      break
    letrasJaInseridas()
    print("-> Você errou pela %i° vez. Tente de novo!"%(tentativas))
    boneco(tentativas)


  ## Verifica se o jogo chegou ao fim
  for i in (lista):
    print(i," ",end="")
  
  if(''.join(lista) == palavraDoSegredo):
    print()
    print("-"*50)
    letrasJaInseridas()
    print("Você acertou!!!!")
    print("O pokemon é : %s"%(palavraDoSegredoOriginal))
    print("*"*50)
    break
  else:
    print()
    print("-"*50)
    entrada = input("Insira outra letra: ")
    validaEntrada(entrada)
    letra = unidecode.unidecode(entrada.upper())
