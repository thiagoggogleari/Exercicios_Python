# Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

valores = []

while True:
  entrada = float(input('Insira a nota para registro: '))
  if entrada == -1:
    print('\n')
    break
  else:
    valores.append(entrada)
    print('Registro efetuado!\n')

qntdValores = len(valores)

print('Foram realizados %i registros'%(qntdValores))
somaTotal = 0

print('Registros: ',end='')
# Imprime os registros e realiza a soma deles para a variável somaTotal
for i in range(len(valores)):
  somaTotal += valores[i]
  if i < len(valores) -1:
    print("{}, ".format(valores[i]),end='')
  else:
    print("{}.".format(valores[i]))

print('\nA soma total das notas é de: {}'.format(somaTotal))

media = somaTotal / len(valores)
print('A média das notas é de: {:.2f}'.format(media))

valoresAcimaMedia = []
valoresAbaixo7 = []

for i in range(len(valores)):
  if valores[i] > media:
    valoresAcimaMedia.append(valores[i])
  if valores[i] < 7:
    valoresAbaixo7.append(valores[i])

print('\nQuantidade de notas acima da média: {}'.format(len(valoresAcimaMedia)))
print('Notas acima da média: ',end='')
for i in range(len(valoresAcimaMedia)):
  if i < len(valoresAcimaMedia)-1:
    print('{}, '.format(valoresAcimaMedia[i]),end='')
  else:
    print('{}.'.format(valoresAcimaMedia[i]))


print('\nQuantidade de notas abaixo de 7: {}'.format(len(valoresAbaixo7)))
print('Notas abaixo de 7: ',end='')
for i in range(len(valoresAbaixo7)):
  if i < len(valoresAbaixo7)-1:
    print('{}, '.format(valoresAbaixo7[i]),end='')
  else:
    print('{}.'.format(valoresAbaixo7[i]))

print('Programa finalizado')
