'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado(inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
num = int(input("Que valor você quer sacar? \n"))
cedulas = [50, 20, 10, 1]
'''

print('-=-' * 10)
print(f'          Banco Itau')
print('-=-' * 10)
valor = int(input('Digite o Valor para Sacar R$:'))
total = valor
dinheiro = 50
tdinheiro = 0
while True:
    if total >= dinheiro:
        total -= dinheiro
        tdinheiro +=1
    else:
        if tdinheiro > 0 :
            print(f'Total de {tdinheiro} Cedulas de \033[32m{dinheiro}\033[m Reais!')
        if dinheiro == 50:
            dinheiro = 20
        elif dinheiro == 20:
            dinheiro = 10
        elif dinheiro == 1:
            dinheiro = 1
        tdinheiro = 0

        if total == 0:
            break
print('-=-' * 10)
print('Retone Sempre ao \033[33mITAU!\033[m')
