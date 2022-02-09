# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
# e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu
# gerar o seguinte arquivo, chamado "usuarios.txt":

# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125

# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que
# gere um relatório, chamado "relatório.txt", no seguinte formato:
# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso

# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB

# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, 
# de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes
# deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do
# percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

# Caminho local
f = open('/content/drive/MyDrive/Colab Notebooks/usuarios.txt')

def converterMB(x):
  megaByte = round(x / 1048576,2)
  return megaByte

def porcentagemUso(usuario,total):
  porcentagem = round((usuario * 100) / total,2)
  return porcentagem

lista = []

# Lê o arquivo e o adiciona a uma lista
for line in f:
  lista.append(line)

# Espaço total utilizado
espacoTotal = 0

# Cálculo do espaço total utilizado
for i in range(len(lista)):
  registro = lista[i].split()
  espacoTotal += converterMB(int(registro[1]))

espaco2 = '*'*5

# Tabela
print('ACME Inc.         Uso do espaço em disco pelos usuários')
print('-----------------------------------------------------------')
print('Nr.  Usuário        Espaço utilizado     % do uso')

for i in range(len(lista)):
  registro = lista[i].split()

  # Imprime o número da sequência
  print('{}    '.format(i+1),end='') 

  # Imprime o nome
  nome = registro[0]
  print('{}'.format(nome),end='')

  # Quantidade de MB utilizada pelo usuário
  atualMB = (converterMB(int(registro[1])))
  espaco1 = ' ' * (28 - len(nome) - len(str(atualMB))) # Espaçamento
  print('{}{} MB'.format(espaco1,atualMB),end='')

  # Porcentagem do uso
  atualPorcentagem = porcentagemUso(atualMB,espacoTotal)
  espaco2 = ' ' * (12 - len(str(atualPorcentagem)))
  print('{}{}%'.format(espaco2,atualPorcentagem))

print('\nEspaço total utilizado: {} MB'.format(espacoTotal))
print('Espaço médio utilizado: {:.2f} MB'.format(espacoTotal / 6)) #verificar espaçamento
