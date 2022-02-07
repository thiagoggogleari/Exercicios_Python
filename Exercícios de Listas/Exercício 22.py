# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer
# um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses
# que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.

# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um
# número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
# necessita da esfera;
# necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual
# a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:

# Quantidade de mouses: 100

# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%

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

print('-' * 70)
print('Quantidade de mouses: {}'.format(len(idMouses)))
print('\nSituação',' '*30,'Quantidade',' ','Percentual')

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
