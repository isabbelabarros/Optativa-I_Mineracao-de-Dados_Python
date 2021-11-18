"""Faça um programa que leia dois valores numéricos e realize a soma, subtração, multiplicação e divisão deles"""

n1 = float(input('Digite o primeiro número: '))

n2 = float(input('Digite o segundo número: '))

print('\n\n********** Calculadora **********\n')
print('Soma: {} + {} = {}'.format(n1, n2, n1+n2))
print('Subtração: {} - {} = {}'.format(n1, n2, n1-n2))
print('Multiplicação: {} * {} = {}'.format(n1, n2, n1*n2))
print('Divisão: {} / {} = {}'.format(n1, n2, n1/n2))