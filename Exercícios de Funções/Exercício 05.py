# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 

# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e
# custo, que é o custo de um item antes do imposto. 
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto,custo):
  res = custo + (taxaImposto * custo)
  return res

taxaImposto = 5/100 # Porcentagem
custo = 4

custo = somaImposto(taxaImposto,custo)

print('Valor com imposto é de R${:.2f}'.format(custo))
