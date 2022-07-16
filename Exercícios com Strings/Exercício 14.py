# 14 Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando 
# outros símbolos em lugar das letras, como números por exemplo. A própria palavra 
# leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura 
# relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir 
# os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de 
# traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia 
# leet speak.

# Comando para instalar a biblioteca unidecode no google colab
#!pip install unidecode

# Este código não tem uma tabela fixa para conversão direta dos caracteres.
# O caractere a ser substituído é escolhido randomicamente

import random
import unidecode

def converteCaractere(letra):
  # Verifca o tamanho da lista da letra correspondente
  tamLista = len(dic[letra])

  # Gera um número de posição aleatório
  numAleatorio = random.randint(0,tamLista - 1)

  # Imprime o caractere convertido
  return dic[letra][numAleatorio]

# Mapa de caracteres a serem utilizados, o caractere correspondente
# é selecionado randômicamente

dic = {
        " ": [" "],
        "a": ["4", "@", "/-\\", "^"],
        "b": ["I3", "8", "13", "|3"],
        "c": ["[", "{", "<", "("],
        "d": [")", "|)", "[)", "|>"],
        "e": ["3", "[-"],
        "f": ["|=", "ph", "|#", "/="],
        "g": ["&", "6", "(_+]", "9", "C-", "gee"],
        "h": ["#", "/-/", "[-]", "]-[", ")-(", "(-)", ":-:", "|-|", "}{"],
        "i": ["1", "[]", "!", "|", "eye", "3y3", "]["],
        "j": [",_|", "_|", "._|", "._]", ",_]", "]"],
        "k": [">|", "|<", "/<", "1<", "|c", "|(", "|{"],
        "l": ["1", "7", "|_", "|"],
        "m": ["/\\/\\", "/V\\", "JVI", "[V]", "[]V[]", "|\\/|", "^^"],
        "n": ["^/", "|\\|", "/\\/", "[\]", "<\\>", "{\\}", "|V", "/V"],
        "o": ["0", "Q", "()", "oh", "[]"],
        "p": ["|*", "|o", "?", "|^", "[]D"],
        "q": ["(_,)", "()_", "2", "O_"],
        "r": ["12", "|`", "|~", "|?", "/2", "|^", "Iz", "|9"],
        "s": ["$", "5", "z", "ehs", "es"],
        "t": ["7", "+", "-|-", "']['", '"|"', "~|~"],
        "u": ["|_|", "(_)", "V", "L|"],
        "v": ["\\/", "|/", "\\|"],
        "w": ["\\/\\/", "VV", "\\N", "'//", "\\\\'", "\\^/", "\\X/"],
        "x": ["><", ">|<", "}{", "ecks"],
        "y": ["j", "`/", "\\|/", "\\//"],
        "z": ["2", "7_", "-/_", "%", ">_", "~/_", "-\_", "-|_"],
}

print("----- Leet spek generator -----")

while True:
  frase = input("Insira uma palavra ou frase para codificar: ")

  # Tratativa da entrada para que os caracteres fiquem minúsculos e sem acentuações  
  frase = unidecode.unidecode(frase.lower())

  stringFinal = ""
  try: 
    # Um laço chama a função 'converteCaractere' enviado um à um para serem convertidos
    for i in range(len(frase)):
        x =converteCaractere(frase[i])
        stringFinal += x
  except:
    print("Números e caracteres especiais não são aceitos!\n")
    continue
  print(stringFinal)
  break 
