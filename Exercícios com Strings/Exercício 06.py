# 6 - Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com
# o nome do mês por extenso.

#    Data de Nascimento: 29/10/1973
#    Você nasceu em  29 de Outubro de 1973.

meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

data = input("Insira data de nascimento (formato dd/mm/aaaa)")

#Verificação simples
while(len(data) != 10): 
  print("*** Verifique se o formato digitado atende os requisitos *** ")
  data = input("\nInsira data de nascimento (formato dd/mm/aaaa)")

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

print("Data de Nascimento: {}/{}/{}".format(dia,mes,ano))
print("Você nasceu em {} de {} de {}.".format(dia,meses[mes-1],ano))
