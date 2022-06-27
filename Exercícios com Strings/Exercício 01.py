# 1 -Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

#   Compara duas strings
#   String 1: Brasil Hexa 2006
#   String 2: Brasil! Hexa 2006!
#   Tamanho de "Brasil Hexa 2006": 16 caracteres
#   Tamanho de "Brasil! Hexa 2006!": 18 caracteres
#   As duas strings são de tamanhos diferentes.
#   As duas strings possuem conteúdo diferente.

string1 = input("Insira a primeira String: ")
string2 = input("Insira a segunda String: ")

print("String 1: %s"%(string1))
print("String 2: %s"%(string2))
print("\nTamanho de \"%s\": %i caracteres"%(string1,len(string1)))
print("Tamanho de \"%s\": %i caracteres"%(string2,len(string2)))


if(len(string1)==len(string2)):
  print("\nAs duas strings possuem o mesmo tamanho")

  # Verifica se as strings tem o mesmo conteúdo  
  contCaracteresIguais = 0;    
  for i in range(len(string1)):
    if(string1[i] == string2[i]):
      contCaracteresIguais += 1

  if(contCaracteresIguais == len(string1)):
    print("As duas strings possuem conteúdos iguais.")
  else:
    print("As duas string possuem conteúdos diferente.")

else:
  print("\nPor terem tamanhos diferentes seus conteúdos também são diferentes")
