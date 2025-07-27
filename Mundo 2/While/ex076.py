'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$ 1000
c) qual é o nome do produto mais barato
'''
pro = soma = cont = menor = conta = 0
mnome = ' '
while True:
    print('-' * 31)
    print('         Loja do Edson')
    print('-' * 31)
    nome = str(input('Nome do Produto:')).strip()
    valor = float(input(f'Valor do(a) {nome} R$:'))
    soma = soma + valor
    cont += 1
    conta += 1
    resp = ' '
    if conta == 1:
        menor = valor
        mnome = nome
    else:
        if valor < menor:
            menor = valor
            mnome = nome
    if valor >= 1000:
        pro += 1
    while resp not in 'SN':
        print('-' * 31)
        resp = str(input('Quer Continuar ?[S/N]')).strip().upper()[0]

    if resp == 'N':
        break
print(f'{' Fim Compras ':=^31}')
print(f'O Total {cont} de Compras Digitadas é de R${soma:.2f}')
print(f'Temos {pro} Produtos Custando Mais de R$1000.00')
print(f'O Produto mais Barato foi {mnome} custando R${menor:.2f}')