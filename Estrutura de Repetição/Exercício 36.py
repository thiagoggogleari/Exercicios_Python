# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
# mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser
# informados também pelo usuário, conforme exemplo abaixo:
#
#    Montar a tabuada de: 5
#    Começar por: 4
#    Terminar em: 7
#
#    Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#    5 X 4 = 20
#    5 X 5 = 25
#    5 X 6 = 30
#    5 X 7 = 35

#    Obs: Você deve verificar se o usuário não digitou o final menor que o inicial

tabuada = 7
inicial = 1
final = 1

tabuada = int(input('Montar a tabuada de: '))
inicial =int(input('Começar por: '))
final = int(input('Terminar em: '))
qntOperacoes = final - inicial + 1
print()

if final < inicial:
  print('Valor final precisa ser maior que o inicial')
else:
  print('Vou montar a tabuada do %i começando em %i e terminando em %i: '%(tabuada,inicial,final))
  for i in range(qntOperacoes):
    print(tabuada,'x',i +inicial,'= %i'%(tabuada * (i + inicial)))
