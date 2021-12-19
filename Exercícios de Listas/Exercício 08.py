# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação
# no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []

for i in range(5):
  entradaIdade = int(input('Qual a idade da %i° pessoa: '%(i+1)))
  idade.append(entradaIdade)

print()
for j in range(5):
  entradaAltura = float(input('Qual a altura da %i° pessoa: '%(j+1)))
  altura.append(entradaAltura)
  

print('\nIdade na ordem inversa: ',end='')
for i in range(len(idade),0,-1):
  if i > 1:
    print(idade[i-1],', ',end='')
  else:
    print(idade[i-1],'.',end='') 
  
print('\nAltura na ordem inversa: ',end='')
for i in range(len(idade),0,-1):
  if i > 1:
    print('{:.2f}, '.format(altura[i-1]),end='')
  else:
    print('{:.2f}.'.format(altura[i-1])) 
