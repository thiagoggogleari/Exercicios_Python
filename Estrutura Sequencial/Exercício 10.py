# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# °F = °C × 1,8 + 32

c = float(input('Qual a temperatura em °C ?'))
f = c * 1.8 + 32

print('%.2f°C equivalem a %.2f°F'%(c,f))