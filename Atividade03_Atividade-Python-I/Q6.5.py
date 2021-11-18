"""Faça um programa que receba um número inteiro n e o fatore."""

n = int(input('Insira o número que será fatorado: '))

i = 2
while i<=n:
    if n%i == 0:
        print(i, end=' . ')
        n //= i
    else:
        i += 1