"""Crie um Python Script que conte quantas vezes cada nome está presente em uma lista [’nome1’, ’nome2’, ...] e armazena essa contagem em um dicionário {’nome1’: xvezes, ’nome2’: yvezes, ....}."""

dicionario = {}
lista = []

lista = ['Cláudia','João','Henrique','Isabela','Sérgio','João','Henrique','Henrique']

for nome in lista:
    if nome in dicionario:
        dicionario[nome] += 1
    else:
        dicionario[nome] = 1
print(dicionario)