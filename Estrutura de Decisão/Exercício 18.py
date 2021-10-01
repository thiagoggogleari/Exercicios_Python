# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

# Este código faz uma validação superficial, ainda é possível fazer combinações inexistentes.

#   Pendências (To Do)
#   * Conferir a quantidade correta de dias em cada mês
#   * Verificar anos bissextos e ajustar calendário do ano

data = input('Insira uma data no formato dd/mm/aaa : ')

lista = data.split("/")
#print(lista)

dia = int(lista[0])
mes = int(lista[1])
ano = int(lista[2])

if dia > 0 and dia <= 31:
  print('Dia inserido OK!')
  if mes > 0 and mes <= 12:
    print('Mês inserido OK!')
    if ano > 1900 and ano < 2021:
      print('Ano inserido OK!')
    else:
      print('Verificar o ano inserido')
  else:
    print('Verificar o mês inserido')
else:
  print('Verificar o dia inserido')