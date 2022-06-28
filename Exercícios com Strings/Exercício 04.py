#4 Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

   # F
   # FU
   # FUL
   # FULA
   # FULAN
   # FULANO

nome = input("Insira o nome: ")
saida = ""

for i in range(len(nome)):
  saida += nome[i]
  print(saida)
