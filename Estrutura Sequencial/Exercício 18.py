# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download
# do arquivo usando este link (em minutos).

tamanho = float(input('Qual o tamanho do arquivo (MB)? '))
velocidade = float(input('Qual a velocidade do link de internet (Mbps)? '))

# Conversão de MB para Mb
tamBits = tamanho * 8

# Quantidade total de segundos
segundos = tamBits / velocidade

# Conversão para minutos e a sobra são os minutos restantes
minutos = segundos // 60
seg = segundos % 60

print('O download irá demorar aproximadamente %i minutos e %i segundos'%(minutos,seg))
