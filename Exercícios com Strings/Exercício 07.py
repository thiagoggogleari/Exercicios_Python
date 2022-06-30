# 7 Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#    quantos espaços em branco existem na frase.
#    quantas vezes aparecem as vogais a, e, i, o, u. 

vogais = ["a","e","i","o","u"]

entrada = input("Insira uma frase: ")
contVogais = 0
contEspacos = 0

for i in range(len(entrada)): 
  
  if(entrada[i] == " "):
    contEspacos += 1

  for j in range(len(vogais)):    
    if(entrada[i] == vogais[j]):
      contVogais += 1


print("Quantidade de espaços: %i"%(contEspacos))
print("Quantidade de vogais: %i"%(contVogais))
