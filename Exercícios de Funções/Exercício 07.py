# Faça um programa que use a função valorPagamento para determinar o valor a ser pago
# por uma prestação de uma conta.

# O programa deverá solicitar ao usuário o valor da prestação e o número de dias 
# em atraso e passar estes valores para a função valorPagamento, que calculará o valor 
# a ser pago e devolverá este valor ao programa que a chamou.

# O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa 
# deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado 
# um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, 
# exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 

# O cálculo do valor a ser pago é feito da seguinte forma. 
# Para pagamentos sem atraso, cobrar o valor da prestação.
# Quando houver atraso, cobrar 3% e multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(valorPrestacao,diasAtraso):
  if diasAtraso > 1:
    resultado = valorPrestacao + (valorPrestacao * 0.3) + (valorPrestacao * 0.1 * diasAtraso)
  else:
    resultado =  valorPrestacao
  return resultado

totalPrestacoesDia = []

while True:
    
  valorPrestacao = float(input('Qual o valor da prestação? '))
  
  if valorPrestacao == 0:
    break

  diasAtraso = int(input('Quantos dias em atraso? '))

  resultado = valorPagamento(valorPrestacao,diasAtraso)

  totalPrestacoesDia.append(resultado)

  print('O valor a ser pago é de {}'.format(resultado))
  print('-'*50)


print()
print('*'*50)
somatoriaDia = 0

for i in range(len(totalPrestacoesDia)):
  somatoriaDia += totalPrestacoesDia[i]

print('\nNo dia foram pagas {} prestações, somadas resultam em R${:.2f}'.format(len(totalPrestacoesDia),somatoriaDia))
