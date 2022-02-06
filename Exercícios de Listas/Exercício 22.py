idMouses = []
defeitos = []

while True:
  print('Para encerrar digite "0"')
  entradaIdMouse = int(input('Insira o número de identificação do Mouse: '))

  if entradaIdMouse == 0:
    print('\nEtapa de Registro finalizada!')
    break
  print('\nTabela de diagnóstico')
  idMouses.append(entradaIdMouse)

  print('*'*70)
  print('1 - Necessita de esfera')
  print('2 - Necessita de limpeza')
  print('3 - Necessita troca do cabo ou conector')
  print('4 - Quebrado ou inutilizado')
  print('*'*70)

  entradaDefeito = int(input('Insira o número equivalente ao diagnóstico do mesmo: '))
  
  while entradaDefeito not in(1,2,3,4):
    print('\nEntrada inválida. Valores válidos são 1, 2, 3 e 4!')
    entradaDefeito = int(input('\nInsira o número equivalente ao diagnóstico do mesmo: '))
  
  defeitos.append(entradaDefeito)
  print('Registro efetuado!\n')

contagem1 = defeitos.count(1)
contagem2 = defeitos.count(2)
contagem3 = defeitos.count(3)
contagem4 = defeitos.count(4)

frase1 = '1 - Necessita de esfera'
frase2 = '2 - Necessita limpeza'
frase3 = '3 - Necessita Troca do cabo ou conector'
frase4 = '4 - Quebrado ou inutilizado'

# Espaçamento
def calculaEspaco1(entrada):
  espaco1 = ' ' * (49 - len(str(entrada)))
  return espaco1

def calculaEspaco2(entrada):
  espaco2 = ' ' * (11 - len(str(entrada)))
  return espaco2

porcentagem1 = round((contagem1 * 100) / len(defeitos),2)
porcentagem2 = round((contagem2 * 100) / len(defeitos),2)
porcentagem3 = round((contagem3 * 100) / len(defeitos),2)
porcentagem4 = round((contagem4 * 100) / len(defeitos),2)

print('\n')
print('-' * 70)
print('Situação',' '*30,'Quantidade',' ','Percentual')

print('{}{}'.format(frase1, calculaEspaco1(frase1)),end='')
print(contagem1,calculaEspaco2(porcentagem1),end='')
print('{}%'.format(porcentagem1))

print('{}{}'.format(frase2, calculaEspaco1(frase2)),end='')
print(contagem2, calculaEspaco2(porcentagem2),end='')
print('{}%'.format(porcentagem2))

print('{}{}'.format(frase3, calculaEspaco1(frase3)),end='')
print(contagem3, calculaEspaco2(porcentagem3),end='')
print('{}%'.format(porcentagem3))

print('{}{}'.format(frase4, calculaEspaco1(frase4)),end='')
print(contagem4, calculaEspaco2(porcentagem4),end='')
print('{}%'.format(porcentagem4))

print('-' * 70)

