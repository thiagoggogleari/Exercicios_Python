# Faça um programa que leia 5 números e informe a soma e a média dos números.

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))
n4 = int(input('Insira o quarto número: '))
n5 = int(input('Insira o quinto número: '))
print()

soma = (n1+n2+n3+n4+n5)
media = soma / 5

print('A soma dos números inseridos é %.2f.'%(soma))
print('A média dos números inseridos é %.2f.'%(media))
