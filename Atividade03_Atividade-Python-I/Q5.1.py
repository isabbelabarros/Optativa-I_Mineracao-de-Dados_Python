"""Crie um Python Script que receba um número inteiro n, correspondente a um valor em reais. Calcule a quantidade mínima de notas que um banco deve fornecer para atingir o valor. Notas disponíveis: 100,00 reais; 50,00 reais; 10,00 reais; 1,00 real."""

n = int(input('Digite o valor desejado: '))

n100 = n//100
n = n%100

n50 = n//50
n = n%50

n10 = n//10
n = n%10

n1 = n//1
n = n%1

print('A quantidade mínima de notas de R$100,00 é ', n100)
print('A quantidade mínima de notas de R$50,00 é ', n50)
print('A quantidade mínima de notas de R$10,00 é ', n10)
print('A quantidade mínima de notas de R$1,00 é ', n1)