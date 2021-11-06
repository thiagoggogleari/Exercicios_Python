# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as
# um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas
# informadas, bem como a média das temperaturas.

lista = []

def validaEntrada(x):
  try:
    float(x)
  except ValueError:
    return False
  return True


print('-- DEPARTAMENTO ESTADUAL DE METEOROLOGIA --')
print('Cadastro de temperatura da região n\n')
while True:
  temp = input('Insira um valor de temperatura(°C) ou digite "S" para sair: ')
  if temp.upper() == 'S':
    break
  if validaEntrada(temp) == False:
    print('Entrada Inválida, digite outro valor')
    continue
  # Insere na lista como tipo 'float'
  lista.append(float(temp))

print()
if len(lista) != 0:
  listaOrdenada = sorted(lista)
  print('A menor temperatura registrada é de %.2f°C'%(listaOrdenada[0]))
  maiorTemp = len(listaOrdenada) - 1
  print('A maior temperatura registrada é de %.2f°C'%(listaOrdenada[maiorTemp]))

  somaTemperatura = 0

  for i in lista:
    somaTemperatura = somaTemperatura + i

  media = somaTemperatura / len(lista)
  print('A média das temperaturas é de %.2f°C'%(media))
else:
  print('Não foi encontrado nenhum registro.')
