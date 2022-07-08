# 10 Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.


unidades = ["zero","um","dois","três","quatro","cinco","seis","sete","oito","nove"]
dezena10 = ["Onze","Doze","Treze","Quatorze","Quinze","Dezesseis","Dezessete","Dezoito","Dezenove"]
dezenas = ["Vinte","Trinta","Quarenta","Cinquenta","Sessenta","Setenta","Oitenta","Noventa"]

numero = int(input("Insira um número de 0 à 99: "))
strNumero = str(numero)

if(len(strNumero) == 1):
  print(unidades[numero].title())
elif(len(strNumero) == 2 and strNumero[0] == "1"):
  print(dezena10[int(strNumero[1]) - 1])
elif(len(str(numero)) == 2 and strNumero[1] == "0"):
  print(dezenas[int(strNumero[0])-2])
elif(len(str(numero)) == 2):
  print(dezenas[int(strNumero[0])-2],"e",unidades[int(strNumero[1])])
else:
  print("Número inválido")
