"""Crie um programa que lê uma mensagem do usuário. Com esta mensagem, faça uma nova omitindo trocando todos os caracteres de nomes próprios por ’*’.
Exemplo: se a mensagem for ’Lucas foi ao shopping com Fernanda assistir aquele filme da Marvel’, a nova mensagem deverá ser ’***** foi ao shopping com ******** assistir aquele filme da ******’. Assuma q"""

frase = str(input('Digite a mensagem: '))
novafrase = ''
iniciamaiuscula = False

for i in frase:
    if i.isupper():
        iniciamaiuscula = True
        novafrase += '∗'
        continue
    if iniciamaiuscula:
        if i.isalpha():
            novafrase += '∗'
            continue
        else:
            novafrase += i
            iniciamaiuscula = False
    else:
        novafrase += i
print(novafrase)