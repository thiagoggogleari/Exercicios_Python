# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).


f = float(input('Qual a temperatura em °F ? '))

# Conversão para graus Celsius
c = 5 * ((f-32) / 9)

print('%.2f°F convertido resulta em: %.2f°C'%(f,c))


