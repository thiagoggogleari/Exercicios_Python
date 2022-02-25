# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado. 

def qntdEntrada(entrada):
  qntd = len(str(entrada));
  print('Este número possui {} dígitos.'.format(qntd))

entrada = int(input('Insira um número inteiro: '))

qntdEntrada(entrada)
