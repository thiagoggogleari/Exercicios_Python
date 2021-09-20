# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Informe seu sexo [M/F]: ')

if sexo.upper() == 'F':
    print('Feminino')
elif sexo.upper() == 'M':
    print('Masculino')
else:
    print('Sexo inválido!')