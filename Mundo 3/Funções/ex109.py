"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep
def maior(*num): #função mais demorada mais efetiva
    cont = maior = menor = 0
    print('-='*20)
    print('Analizando os valores passados . . . ')
    for valor in num:
        print(f'{valor}' ,end=' ',flush=True)
        sleep(0.5)
        if cont == 0:
            maior = menor = valor
        else:
            if valor > maior:
                maior = valor
    print(f'Ao todo foram {len(num)} Valores Passados')
    print(f'E o Maior valor digitado foi {maior}')
    print(f'E o menor valor digitado foi {min(num)}')
#Inicio:
maior(4,6)
maior(5,6,8)
maior(8,20)
maior(9,1,5,8,10)
maior(0)




'''def maior(*num):     # uma forma de fazer o funcção mais simples!
    print('Analizando os valores passados . . . ')
    print(f'{num} Ao todo foram {len(num)} Valores Passados')
    print(f'O Maior valor informado foi {max(num)}')'''