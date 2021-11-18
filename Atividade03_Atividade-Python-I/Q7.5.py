""" Escreva um programa que leia um número N. Em sequência, ele deve ser N números e armazená-los em uma lista."""

lista = []

N = int(input('Digite um número: '))

for i in range(N):
    x = float(input('Digite o {} número: '.format(i+1)))
    lista.append(x)
print(lista)

