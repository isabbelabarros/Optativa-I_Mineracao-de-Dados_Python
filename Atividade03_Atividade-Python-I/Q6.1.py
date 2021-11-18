"""Faça um código que receba um número n do usuário e imprima os n primeiros números da sequência de Fibonacci."""

t1 = 0
t2 = 1
cont = 3

n = int(input('Digite a quantidade de números que serão mostrados da sequência de Fibonacci: '))

print('Sequência de Fibonacci: ')
print('{} - {}'.format(t1, t2), end='')

while cont <= n:
    tn = t1 + t2
    t1 = t2
    t2 = tn
    cont += 1
    print(' - {}'.format(tn), end='')