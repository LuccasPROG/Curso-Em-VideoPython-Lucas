''' Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo'''





n = int(input('Digite um Numero:'))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')

print(f'\n\033[mO Numero {n} foi Divisivel {tot} Vezes')
if tot == 2:
    print('\033[1;33mPor Isso ele é um Numero Primo!!\033[m')
else:
    print('\033[1;31mPor Isso ele Não é um Numero Primo!!\033[m')