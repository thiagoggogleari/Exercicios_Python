# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# Biblioteca necessário para remover acentuação
import unidecode

letra = input('Insira uma letra: ')
teste = letra.isalpha()

# Caso o caractere digitado não seja uma letra, ele entra neste loop
while teste is not True:
    print('\nO caractere precisa ser uma letra!')
    letra = input('Insira uma letra: ')
    teste = letra.isalpha() 

# Caso a letra tenha acento, ele é removido
letraSemAcento = unidecode.unidecode(letra)

# Verificação se é vogal
if letraSemAcento.lower() in ('a','e','i','o','u'):
    print('A letra é uma Vogal')
else:
    print('A letra é uma Consoante')
