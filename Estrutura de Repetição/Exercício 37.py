dicionario = {}
dicionario = {'Codigo':[],'Altura':[],'Peso':[]}

while True:

  codigo = int(input('Insira o código do cliente: '))
  if codigo == 0:
    break
  altura = float(input('Insira a altura do cliente: '))
  peso = float(input('Insira o peso do cliente: '))

  dicionario['Codigo'].append(codigo)
  dicionario['Altura'].append(altura)
  dicionario['Peso'].append(peso)
  print('Registro efetuado\n')

qntdRegistros = len(dicionario['Altura'])

print()
print('-'*13,'Levantamento de dados','-'*13)

# Maior e menor altura
print('*'*50)
ordenadoAltura = sorted(dicionario['Altura'])
print('Menor altura: %.2fmts'%(ordenadoAltura[0]))
print('Maior altura: %.2fmts'%(ordenadoAltura[qntdRegistros -1]))
print('*'*50)

# Maior e menor peso
ordenadoPeso = sorted(dicionario['Peso'])
print('Menor peso: %.2fkg'%(ordenadoPeso[0]))
print('Maior peso: %.2fkg'%(ordenadoPeso[qntdRegistros -1]))
print('*'*50)

somaDasAlturas = 0
somaDosPesos = 0

for i in range(qntdRegistros):
      somaDasAlturas = somaDasAlturas + dicionario['Altura'][i] 
      somaDosPesos = somaDosPesos + dicionario['Peso'][i]

print('A média das alturas dos clientes é de: %.2fmts'%(somaDasAlturas / qntdRegistros))
print('A média de peso dos clientes é de: %.2fkg'%(somaDosPesos / qntdRegistros))
print('*'*50)
