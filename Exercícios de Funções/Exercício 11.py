# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a 
#  data e retorne NULL caso a data seja inválida.

# Validação simples de data. O ano não foi considerado.
def validaData(lista): 
  if (int(lista[0]) < 1 or int(lista[0]) > 31):
    print("Data inválida")
    return False
  elif (int(lista[1]) < 1 or int(lista[1]) > 12):
    print("Data inválida")
    return False
  else:
    return True

meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
x = False;


while (x == False):
  data = input('Insira a data: ')
  lista = data.split('/')

  x = validaData(lista);

string = lista[0] + " de " + meses[int(lista[1])-1] + " de " + lista[2]
print(string)
