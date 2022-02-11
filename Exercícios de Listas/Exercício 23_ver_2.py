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

# Caminho página web, raw github
master = 'https://raw.githubusercontent.com/thiagoggogleari/exercicios_python/1e7ab8e5758c008ddfb2810d5c3b1338698e6b9c/Exerc%C3%ADcios%20de%20Listas/usuarios(ex_23).txt'

# Como é a primeira vez que faço uma soliciação http para integrar um documento .txt no código,
# procurei por um exemplo que fizesse tal solicitação. É este a serguir: 
#-----------------------------
import base64
import requests

req = requests.get(master)
req = req.text
#-----------------------------

# Divide o texto em uma lista
registro = req.split()

def converterMB(x):
  megaByte = round(x / 1048576,2)
  return megaByte

def porcentagemUso(usuario,total):
  porcentagem = round((usuario * 100) / total,2)
  return porcentagem

# Trecho para cálculo do espaço total utilizado
espacoTotal = 0
contador = 1 # para posição na lista
for i in range(6):
  espacoTotal = espacoTotal + converterMB(int(registro[contador]))
  contador += 2 # Vai pulando de 2 em 2 a posição 


print('ACME Inc.         Uso do espaço em disco pelos usuários')
print('-----------------------------------------------------------')
print('Nr.  Usuário        Espaço utilizado     % do uso')

contador = 0 # para posição na lista
for i in range(6):
  nome = registro[contador]
  numero = registro[contador + 1]

   # Imprime o número da sequência
  print('{}    '.format(i+1),end='') 

  # Imprime o nome
  nome = registro[contador]
  print('{}'.format(nome),end='')
  
  # Quantidade de MB utilizada pelo usuário
  atualMB = (converterMB(int(registro[contador+1])))
  espaco1 = ' ' * (28 - len(nome) - len(str(atualMB))) # Espaçamento
  print('{}{} MB'.format(espaco1,atualMB),end='')

  # Porcentagem do uso
  atualPorcentagem = porcentagemUso(atualMB,espacoTotal)
  espaco2 = ' ' * (12 - len(str(atualPorcentagem)))
  print('{}{}%'.format(espaco2,atualPorcentagem))

  contador += 2 # Vai pulando de 2 em 2 a posição 

print('\nEspaço total utilizado: {} MB'.format(espacoTotal))
print('Espaço médio utilizado: {:.2f} MB'.format(espacoTotal / 6))
