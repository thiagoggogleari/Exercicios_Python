#  Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
#  Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível.
#  Calcule e mostre:

# O modelo do carro mais econômico;
# Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância
# de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro.
# Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo.
# Os dados são fictícios e podem mudar a cada execução do programa.
#Comparativo de Consumo de Combustível

# Veículo 1
# Nome: fusca
# Km por litro: 7
# Veículo 2
# Nome: gol
# Km por litro: 10
# Veículo 3
# Nome: uno
# Km por litro: 12.5
# Veículo 4
# Nome: Vectra
# Km por litro: 9
# Veículo 5
# Nome: Peugeout
# Km por litro: 14.5

# Relatório Final
#  1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
#  2 - gol             -   10.0 -  100.0 litros - R$ 225.00
#  3 - uno             -   12.5 -   80.0 litros - R$ 180.00
#  4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
#  5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
# O menor consumo é do peugeout.



# Esta função verifica se o número é inteiro ou decimal
# Se faz necessário para o dimensionamento de espaços antes de mostrar 'valorGastoCombustivel'

def verificaInteiro(entrada):
  x = float(entrada)
  y = int(entrada)

  if x == y:
    # print('Inteiro')
    return 1
  else:
    # print('Decimal')
    return 0
 

kmViagem = 1000
precoGasolina = 2.25

listaCarros = ['Fusca','Gol','Vectra','Opala','Fiat Uno']
listaConsumo = [7,10,8,5,12.5]
litrosParaViagem = []

# Variáveis para verificação do menor consumo
maiorNumero = 0
veiculoMenorConsumo = 0

# Quantidade de litros necessários para viagem em cada carro
for i in range(len(listaCarros)):
  x = round((kmViagem / listaConsumo[i]),1)
  litrosParaViagem.append(x)

  # Verifica o veículo com menor consumo
  if listaConsumo[i] > maiorNumero:
    veiculoMenorConsumo = i
    maiorNumero = listaConsumo[i]

print('Relatório Final')

for i in range(len(listaCarros)):

  # Espaçamento da tabela
  espaco1 = ' ' * (11 - len(listaCarros[i]))
  espaco2 = ' ' * (7 - len(str(listaConsumo[i])))
  espaco3 = ' ' * (8 - len(str(litrosParaViagem[i])))

  # Cálculo do último espaçamento, necessário validar para ajuste devido ao número de casas decimais
  valorGastoCombustivel = round(litrosParaViagem[i] * precoGasolina,2)
  espacoExtra = verificaInteiro(valorGastoCombustivel)
  espaco4 = ' ' * (8 - len(str(valorGastoCombustivel)) - espacoExtra)

  print('{} - {}'.format(i+1,listaCarros[i]),end='')
  print('%s'%(espaco1),end='')
  print(' -',end='')
  print('%s'%(espaco2),end='')
  print('{}'.format(listaConsumo[i]),end='')
  print(' -',end='')
  print('%s'%(espaco3),end='')
  print('{}'.format(litrosParaViagem[i]),end='')
  print(' litros - R$',end='')
  print('%s'%(espaco4),end='')
  print('{:.2f}'.format(valorGastoCombustivel),end='')
  print()

print('\nO veículo com menor consumo é o {}'.format(listaCarros[veiculoMenorConsumo]))


##############################################################################
# Resposta obtida do programa

# Relatório Final
# 1 - Fusca       -      7 -   142.9 litros - R$  321.53
# 2 - Gol         -     10 -   100.0 litros - R$  225.00
# 3 - Vectra      -      8 -   125.0 litros - R$  281.25
# 4 - Opala       -      5 -   200.0 litros - R$  450.00
# 5 - Fiat Uno    -   12.5 -    80.0 litros - R$  180.00

# O veículo com menor consumo é o Fiat Uno
##############################################################################
