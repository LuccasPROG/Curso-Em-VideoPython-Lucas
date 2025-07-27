'''
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos precos,
na sequência

No final, mostre uma listagem de precos,
organizando os dados em forma tabular
'''

produto = ('Lapis', 3.75,
           'borracha', 2.50,
           'leite', 7.14,
           'macarrao', 4.15,
           'chocolate',14.11,
           'computador', 3500,
           'ventilador', 199.99,
           'Coberta', 39.80,
           'Roupa', 50)
print('-=-'*20)
print(f'{"LISTAGEM DE PRODUTOS":^60}')
print('-=-'*20)
for item in range(0, len(produto)):
    if item % 2 == 0:
        print(f'{produto[item]:.<50}',end='')
    else:
        print(f'R${produto[item]:<10.2f}')
print('-=-'*20)