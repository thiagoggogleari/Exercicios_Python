# 2 - Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida
# mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao 
# informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome = input("Digite seu nome:")
nomeInvertido = ""

for i in range(len(nome), 0, -1):
  lista.append(nome[i-1])
  nomeInvertido += nome[i-1]
  
print("Nome invertido:",nomeInvertido.upper())
