# 8 - Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda 
# ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. 
# A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia 
# uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

# Exemplos
# A base do teto desaba
# A cara rajada da jararaca
# Acuda cadela da Leda caduca
# A dama admirou o rim da amada
# A Daniela ama a lei? Nada!


#frase = "A Daniela ama a lei? Nada!"
frase = input("Insira uma frase para verificar: ")
tamFrase = len(frase)
fraseFormatada = ""

ignorar = [" ",".","&","/","?","!"]
 
acento_A = ["á","à","ã","â","ä"]
acento_E = ["é","è","ê","ë"]
acento_I = ["í","ì","î","ï"]
acento_O = ["ó","ò","õ","ô","ö"]
acento_U = ["ú","ù","û","ü"]

def validaLetra(caractere):
  if(caractere in acento_A):
    return "a"
  elif(caractere in acento_E):
    return "e"
  elif(caractere in acento_I):
    return "i"
  elif(caractere in acento_O):
    return "o"
  elif(caractere in acento_U):
    return "u"
  else:
    return caractere

print("A frase é:\n%s"%(frase))


# Remove espaços e caracteres contidos na lista "ignorar"
for i in range(len(frase)):
  if(frase[i] not in ignorar):
    fraseFormatada += frase[i]

print("\nA frase sem espaços e caracteres especiais [\" \",\".\",\"&\",\"/\",\"?\",\"!\"] fica:")
print(fraseFormatada)
# Para melhorar a vizualização outros laços

caractere = ""
fraseFormatoFinal = ""
# Remove a acentuação através da chamada de função 'validaLetra'
# Adicona o caractere minúsculo à variável 'fraseFormatoFinal'
for i in range(len(fraseFormatada)):
  caractere = validaLetra(fraseFormatada[i])
  fraseFormatoFinal += caractere.lower()

print("\nA frase sem acentos fica:")
print(fraseFormatoFinal)


contTotalIguais = 0
contPosInvertido = len(fraseFormatoFinal)

# Faz o comparativo entre os caracteres, primeiro com último, segundo com penúltimo...
# Caso os caracteres sejam iguais é incrementado o contador 'contTotalIguais'
for i in range(len(fraseFormatoFinal)):
  ## Imprime os caracteres que estão sendo analizados
  #print(frase[i])
  #print(frase[contPosInvertido])
  #print("")

  # Inicia decrementando em 1, devido a contagem de posições começar em '0'
  contPosInvertido -= 1

  if(fraseFormatoFinal[i] == fraseFormatoFinal[contPosInvertido]):
    contTotalIguais += 1

print("\nQuantidade de letras: %s"%(contTotalIguais))
if(contTotalIguais == len(fraseFormatoFinal)):
  print("É um palíndromo!")
else:
  print("Não é um palíndromo!")
