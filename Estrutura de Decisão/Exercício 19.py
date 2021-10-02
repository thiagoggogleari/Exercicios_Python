#   Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#   Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#   326 = 3 centenas, 2 dezenas e 6 unidades
#   12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

entrada = float(input('Insira um número menor que 1000: '))

while entrada >= 1000: 
    print('O número deve ser menor do que 1000!')
    entrada = float(input('Insira um número menor que 1000: '))

# Caso o número seja negativo, o torna positivo
num = abs(entrada)

# Realiza uma divisão em que o resultado seja um número inteiro456
# O resultado é a quantidade de centenas no número
centena = num // 100

# Realiza o módulo % de 100, o resultado é a sobra da operação anterior
sobraCentena = num % 100

# Faz uma divisão (sem sobra) pelo número 10, para descobrir a quantidade de dezenas
dezena = sobraCentena // 10
# É realizado o módulo de 10 para se obter as unidades.
unidade = sobraCentena % 10

# Adiciona a uma variável a palavra no singular ou plural
if centena > 1:
    palavraCentena = 'centenas'
if dezena > 1:
    palavraDezena = 'dezenas'
if unidade > 1:
    palavraUnidade = 'unidades'

if centena == 1:
    palavraCentena = 'centena'
if dezena == 1:
    palavraDezena = 'dezena'
if unidade == 1:
    palavraUnidade = 'unidade'


print('%i = '%(entrada),end='')

# Caso tenha algum valor na centena imprime: 
if centena > 0:
    print('%i %s'%(centena,palavraCentena),end='')
    # Verifica se há outros valores a serem mostrados, e imprime caractere separdor de acordo
    if dezena > 0 and unidade > 0:
        print(', ',end='')
    if dezena > 0 and unidade == 0:
        print(' e ',end='')
    if dezena == 0 and unidade > 0:
        print( 'e ',end='')

# Caso tenha algum valor na dezena imprime: 
if dezena > 0:
    print('%i %s'%(dezena,palavraDezena),end='')
    if unidade > 0:
        print(' e ',end='')

# Caso tenha algum valor na unidade imprime: 
if unidade > 0:
    print('%i %s'%(unidade,palavraUnidade),end='')

if num == 0:
    print('É um número nulo.')

print('.\n')