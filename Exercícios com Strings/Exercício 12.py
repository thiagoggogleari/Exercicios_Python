# 12 Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número
# no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. 
# O usuário pode informar o número com ou sem o traço separador.

# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

telefone = input("Insira o telefone: ")
soNumeros = ""
print()

# Monta o número com o digito 3 e com o caractere "-"
def montarNumero(num):
  numNovo = ""
  for i in range(len(num)):
    if(i == 0):
      numNovo += "3"
    if(i == 3):
      numNovo += "-"
    numNovo += num[i]
  return numNovo

### Início 

# Se o caractere é um número, adiciona à String 'soNumeros', caso contrário, ignora
for i in range(len(telefone)):
  if(telefone[i].isdigit() == True):
    soNumeros += telefone[i]

print("Valida e corrige número de telefone")

if(len(soNumeros) == 7):
  print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente")
  print("Telefone corrigido sem formatação: 3%s"%(soNumeros))
  print("Telefone corrigido com formatação: " + montarNumero(soNumeros))
  
elif (len(soNumeros) == 8):
  print("O número já possui 8 digitos")
else:
  print("Verifique o número inserido")
