# 43
# O cardápio de uma lanchonete é o seguinte:

# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00

# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral
# do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.


listaCodigo = [100,101,102,103,104,105]
listaPreco = [1.20,1.30,1.50,1.20,1.30,1]
diciCardapio = {100:['Cachorro Quente',1.20],
                101:['Bauru Simples',1.30],
                102:['Bauru com ovo',1.50],
                103:['Hambúrguer',1,20],
                104:['Cheeseburguer',1.30],
                105:['Refrigerante',1.00]                
                }
espaco1 = 22
espaco2 = 10
espaco3 = 5

listaPedido = []
listaQntd = []

# Cardápio
print('Especificação',end='')
print(' '*(espaco1 - len('Especificação')),end="")
print('Código',end='')
print(' '*(espaco2 - len('Código')),end='')
print('Preço',end='')
print(' '*(espaco3 - len('Preço')))
print()

# Realiza o espaçamento correto do cardápio
especificacao = ['Cachorro Quente','Bauru Simples','Bauru com ovo','Hambúrguer','Cheeseburguer','Refrigerante']
for i in range(len(especificacao)):
  print(especificacao[i], end='')
  print(' '*(espaco1 - len(especificacao[i])),end='')
  
  print(listaCodigo[i],end='')
  print(' '*(espaco2 - len(str(listaCodigo[i]))),end='')

  print('R$%.2f'%(listaPreco[i]))



# Pedido
while True:
  print("\nPara encerrar o pedido digite algum código que não consta no cardápio")

  pedido = int(input('Qual o código do pedido? '))
  if pedido < 100 or pedido > 105:
    break

  qntd = int(input('Qual a quantidade? '))

  listaPedido.append(pedido)
  listaQntd.append(qntd)
  


# Nota 
total = 0

print('\n\n--------- Nota ---------')
for i in range(len(listaPedido)):
  # Lista recebe nome e preço do produto com base em seu código
  listaAtual = diciCardapio[listaPedido[i]]

  print('Lanche: %s'%(listaAtual[0]))
  
  print('Preço: R$%.2f'%(listaAtual[1]))
  
  print('Quantidade: %i'%(listaQntd[i]))
    
  print('Sub-Total:R$%.2f'%(listaAtual[1] * listaQntd[i]))
  total = total + (listaAtual[1] * listaQntd[i])
  print()  

print('-'*24)
print('Total: R$%.2f'%(total))
print('-'*24)
