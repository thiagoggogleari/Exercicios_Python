# 9 Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e 
# indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação. 

# Fonte de onde obtive como o cálculo é feito
# https://www.macoratti.net/alg_cpf.htm#:~:text=O%20algoritmo%20de%20valida%C3%A7%C3%A3o%20do,%3A%20111.444.777%2D05


print("Verificação de CPF")

cpf = input("Insira um cpf no formato xxx.xxx.xxx-xx : ")
while(len(cpf) != 14):
  print("Verifique a quantidade de dígitos informados!\n")
  cpf = input("Insira um cpf no formato xxx.xxx.xxx-xx : ")

print("\nO cpf inserido é: %s"%(cpf))
print("\n------------------Análise -----------------\n")

def verificaCaracteres():
  contCarac = 0
  if(cpf[3] == "."):
    contCarac += 1
  if(cpf[7] == "."):
    contCarac += 1
  if(cpf[11] == "-"):
    contCarac += 1
  if(contCarac == 3):
    print("Caracteres de separação OK")
    return True
  else:
    print("Caracteres de separação inválidos!")
    return False


def verificaQntdNumeros():  
  contNumeros = 0
  
  for i in range(len(cpf)):
    if(cpf[i].isdigit() == True):
      contNumeros += 1

  if(contNumeros == 11):
    print("Quantidade de números Ok")
    return True
  else:
    return False
    
def calcPrimeiroDigito():
  listaNumConcatenados = []
  listaMultiplicador = [10,9,8,7,6,5,4,3,2]

  # Monta uma lista com os 9 primeiro números que compões o cpf digitado
  for i in range(11):
    if(cpf[i].isdigit()):
      listaNumConcatenados.append(int(cpf[i]))

  somatoria = 0  
  for i in range(9):
    # A variável 'x' realiza a multiplicação dos números do cpf por seu multiplicador correspondente.
    x = (listaNumConcatenados[i] * listaMultiplicador[i])
    somatoria += x
    #print(x)  
  #print(somatoria)

  resto = somatoria % 11
  if(resto < 2):
    digito1 = 0
  else:
    digito1 = 11 - resto
  print("\nO primeiro digito verificador calculado é %i"%(digito1))

  if(digito1 == int(cpf[12])):
    print("Primeiro digito verificador - OK")
    return True
  else:
    print("Primeiro digito verificador - Inválido!")
  return False
  
def calcSegundoDigito():
  listaNumConcatenados = []
  listaMultiplicador = [11,10,9,8,7,6,5,4,3,2]

  contador = 0
  # Monta uma lista com os 11 primeiro números que compões o cpf digitado
  for i in range(13):
    if(cpf[i].isdigit()):
      listaNumConcatenados.append(int(cpf[i]))
      
  somatoria = 0  
  for i in range(10):
    # A variável 'x' realiza a multiplicação dos números do cpf por seu multiplicador correspondente.
    x = (listaNumConcatenados[i] * listaMultiplicador[i])
    somatoria += x
  
  resto = somatoria % 11
  if(resto < 2):
    digito2 = 0
  else:
    digito2 = 11 - resto

  print("\nO segundo digito verificador calculado é %i"%(digito2))
  if(digito2 == int(cpf[13])):
    print("Segundo digito verificador - OK")
    return True
  else:
    print("Segundo digito verificador - Inválido!")
    return False


###### Início do programa ######

# Explicação de cada função

# Valida se há 3 caracteres de pontuação presentes no cpf
#verificaCaracteres()

# Valida quantidade de números presentes   
#verificaQntdNumeros()

# Calcula o primeiro digito verificador e o compara com o do cpf informado
#calcPrimeiroDigito()

# Calcula o segundo digito verificador e o compara com o do cpf informado
#calcSegundoDigito()

if(verificaCaracteres() == True and verificaQntdNumeros() == True and calcPrimeiroDigito() == True and calcSegundoDigito() == True):
  print("\n*** CPF VÁLIDO ***")
else:  
  print("*** CPF INVÁLIDO ***")

print("\n-------------- Fim da análise --------------")
