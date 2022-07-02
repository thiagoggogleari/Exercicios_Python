# 9 Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

numero = int(input("Insira um número: "))
numero = str(numero)

for i in range(len(numero),0,-1):
  print(numero[i-1],end="")
