# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!",
#    "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('M - Matutino')
print('V - Vespertino')
print('N - Noturno')


turno = input('Qual turno você estuda? [M/V/N] ')

while turno.upper() not in ('M','V','N'):
  print('Valor inválido!')
  turno = input('Qual turno você estuda? [M/V/N] ')

if turno.upper() == 'M':
  print('Bom dia')
elif turno.upper() == 'V':
  print('Boa tarde')
else:
  print('Boa noite')
