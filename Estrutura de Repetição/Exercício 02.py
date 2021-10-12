# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações

login = input('Informe o login de usuário: ')
senha = input('Informe a senha de acesso: ')

while login == senha:
  print('Login e senha não podem ser iguais!')
  login = input('Informe o login de usuário: ')
  senha = input('Informe a senha de acesso: ')

print('Acesso concedido')
