"""
Crie um programa que tenha uma função chamada sorteados e sorteia
#uma e uma função chamada par e depois soma os pares!
"""
from random import randint
from time import sleep
def sorteados(num):
    print(f'Sorteando {len(num)} valores da lista:',end=' ')
    for valor in num:
        sleep(0.5)
        print(f'{valor} ',end='', flush=True)
    print('Pronto!')
def pares(par):
    soma = 0
    for valor in par:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores Pares de {par}, temos {soma}!')
#Inicio:
sorte = list()
for c in range(1,6):
    sorte.append(randint(1,10))
sorteados(sorte)
pares(sorte)