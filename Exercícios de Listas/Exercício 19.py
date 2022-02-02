# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

votos = []

while True: 
  entrada = int(input('Qual o melhor sistema operacional para uso em servidores? '))
  if entrada == 0:
      break
  if entrada in (1,2,3,4,5,6):
    votos.append(entrada)
  else:
    print('Entrada Inválida')


print('\nForam computados {} voto(s).'.format(len(votos)))
#print('Os votos registrados foram: ')
#print(votos)

maisVotado = 0
qntdVotosMaisVotado = 0
totalVotos = [] # Contagem total de votos
empatados = []


for i in range(6): # Quantidade de sistemas operacionais
  somatoriaVotos = votos.count(i+1) # Conta o voto e adiciona o resultado a lista totalVotos
  totalVotos.append(somatoriaVotos)

  if somatoriaVotos > qntdVotosMaisVotado:  # Verifica qual foi o mais votado
    maisVotado = i + 1 
    qntdVotosMaisVotado = somatoriaVotos

for i in range(6):
  if totalVotos[i] == qntdVotosMaisVotado:
    empatados.append(i+1)

# print('Empatados')
# print(empatados)
 
listaSistemas = ['Windows Server','Unix','Linux','Netware','Mac OS','Outro']
sistema = listaSistemas[maisVotado -1]
 

# Espaçamento da tabela
espacos1 = 29
espacos2 = 8

print('\nSistema Operacional     Votos      %')
print('-------------------     -----    -----')

for i in range(len(listaSistemas)):
  porcentagem = round((totalVotos[i] * 100) / len(votos),1)
  print('{}{}{}{}{}%'.format(listaSistemas[i],' '*(espacos1 - len(listaSistemas[i]) - len(str(totalVotos[i]))),totalVotos[i],' '*(espacos2 - len(str(porcentagem))),porcentagem))

print('-------------------     -----    -----')
print('Total',' ' *21, len(votos))

# Caso haja empate entra na primeira condição
if len(empatados) > 1:
  print('\nHouve empate na primeira colocação entre os sistemas:')
  for i in range(len(empatados)):
    # Puxa da lista de sistemas conforme o número equivalente do sistema
    print(listaSistemas[empatados[i] -1])
  print('\nCada um com {:.1f}% dos votos.'.format((qntdVotosMaisVotado * 100)/len(votos)))

else:
  print('\nO sistema operacional mais votado foi o {}, com {} voto(s), correspondendo a {:.1f}% dos votos.'.format(sistema,qntdVotosMaisVotado,(qntdVotosMaisVotado * 100)/len(votos)))
