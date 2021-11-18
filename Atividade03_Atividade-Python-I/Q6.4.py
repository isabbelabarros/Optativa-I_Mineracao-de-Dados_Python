"""Faça um programa que liste para o usuário um menu com quatro opções, sendo cada uma referente à uma operação matemática básica. Após o usuário ter escolhido a opção, leia dois valores e realiza a operação selecionada."""

print('\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n')

opcao = int(input('Escolha a opção desejada: '))

n1 = float(input('Digite o primeiro número: '))

n2 = float(input('Digite o segundo número: '))

if opcao == 1:
    print('{} + {} = {}'.format(n1,n2,n1+n2))
elif opcao == 2:
    print('{} - {} = {}'.format(n1,n2,n1-n2))
elif opcao == 3:
    print('{} * {} = {}'.format(n1,n2,n1*n2))
elif opcao == 4:
    print('{} / {} = {}'.format(n1,n2,n1/n2))
else:
    print('Opção inválida!')