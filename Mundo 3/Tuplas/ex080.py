'''
Crie um programa que vai gerar cinco números aleatórios 
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados
e também indice o menor e o maior valor que estão na tupla
'''
from random import randint
aleatorio = (randint(1,10),randint(1,10),randint(1,10),
             randint(1,10),randint(1,10))
print(f'Os Valores Sorteados foram :',end='')
for a in aleatorio:
    print(f'{a} ',end='')
print(f'\nO Maior Numero Digitado foi :{max(aleatorio)}') #funciona so em tuplas max = numero maior digitado !
print(f'O Menor Numero Digitado foi :{min(aleatorio)}')#funciona so em tuplas min = menor numero digitado !