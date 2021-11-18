"""Com o programa acima, imprima: A soma dos itens, a média dos valores, o maior e o menor valor."""

lista = []
soma = 0
media = 0

N = int(input('Digite um número: '))

for i in range(N):
    x = float(input('Digite o {} número: '.format(i+1)))
    lista.append(x)

menor = lista[0]
maior = lista[0]

for i in lista:
    soma += i
    if menor >= i:
        menor = i
    if maior <= i:
        maior = i

media = soma/N

print('\n')
print(lista)
print('Soma: {}'.format(soma))
print('Média: {}'.format(media))
print('Menor: {}'.format(menor))
print('Maior: {}\n'.format(maior))