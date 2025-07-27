''' Crie um programa que leia dois valores e mostre um menu
na tela:

1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa

Seu programa deverá realizar a operação solicitada em cada caso '''
from time import sleep
n1 = int(input('Digite o Primeiro Valor:'))
n2 = int(input('Digite o Segundo Valor:'))
opcao = 0
while opcao != 5:
    print('-=' * 20)
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos Números
    [5]Sair Do Programa''')
    opcao = int(input('Digite Sua Opção:'))
    print('Analizando . ')
    sleep(1)
    if opcao == 1:
        soma = n1 + n2
        print('-='*20)
        print(f'A soma entre {n1} e {n2} é igual a {soma}')
    elif opcao == 2:
        m = n1 * n2
        print('-=' * 20)
        print(f'A Multiplicado entre {n1} e {n2} é igual a {m}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O Maior Numero Digitado foi de: {n1}')
        else:
            print(f'O Maior numero Digitado Foi de: {n2}')
    elif opcao == 4:
        print('Informe os Numeros Novamente!')
        n1 = int(input('Digite o Primeiro Valor:'))
        n2 = int(input('Digite o Segundo Valor:'))
    elif opcao == 5:
        print('Encerrando .')
        sleep(2)
        print('Encerrando . .')
        print('-='*20)
    else:
        print('Numero Invalido,  Tente Novamente.')
    sleep(2)
print('Tenha um Bom Dia!')