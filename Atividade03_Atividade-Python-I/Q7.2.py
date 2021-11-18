"""Crie um Python Script que realize o mesmo procedimento da questão anterior. No entanto, ao invés do conteúdo da lista nomes ser atribuído no próprio script, faça uma estrutura de repetição na qual ela leia uma string do usuário e adicione os nomes digitados por ele, um de cada vez, na lista nomes. O término da adição de nomes deve ser indicado quando o usuário inserir uma string vazia (”)."""

dicionario = {}
lista = []
nome = '-'

while nome != '':
    nome = str(input('Digite um nome: '))
    lista.append(nome)

lista.remove('')

for nome in lista:
    if nome in dicionario:
        dicionario[nome] += 1
    else:
        dicionario[nome] = 1
print(dicionario)