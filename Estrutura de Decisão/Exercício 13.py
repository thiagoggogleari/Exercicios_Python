# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer 
# valor inválido.

dia = int(input('Digite o dia da semana: '))

while dia not in(1,2,3,4,5,6,7):
    print('Valor inválido')
    dia = int(input('Digite o dia da semana: '))


semana = ['Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado','Domingo']

# Como a lista tem início do índice em 0, é diminuido em 1 a variável dia para tabela ser expressa corretamente
print('O dia da semana correspondente é: %s'%(semana[dia-1]))