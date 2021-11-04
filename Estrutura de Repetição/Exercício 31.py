# 31
# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências
# Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido
# de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final
# da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
# para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
# para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

# Lojas Tabajara 
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00


while True:
  lista = []
  entrada = 1 # iniciado em 1 para que o loop do while não se encerre
  numProduto = 1 # contador que vai incrementando a númeração dos produtos
  print('*'*20,'NOTA DE COMPRAS','*'*20)

  while entrada != 0:
    entrada = float(input('Insira o preço da %i° mercadoria: '%(numProduto)))
    lista.append(entrada)
    numProduto += 1

  # Remove o último registro da lista ('0')
  lista.remove(0)
  print()


  numProduto = 1 # contador que vai incrementando a númeração dos produtos
  valorTotal = 0

  for i in lista:
    print('Produto %i: R$%.2f'%(numProduto,i))
    valorTotal = valorTotal + i
    numProduto += 1

  print()
  print('Total: R$%.2f'%(valorTotal))


  pago = float(input('Qual o valor pago em dinheiro? '))

  if (pago >= valorTotal):
    print('Troco: R$%.2f'%(pago - valorTotal))
  else:
    print('Falta R$%.2f para a compra ser realizada!'%(valorTotal - pago))

  print('*'*18,'REGISTRO FINALIZADO','*'*18,'\n\n')
