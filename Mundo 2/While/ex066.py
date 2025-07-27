''' Faça um programa que leia um número qualquer e mostre
o seu fatorial 

exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
'''
from math import factorial
n = int(input('Digite um numero para calcular o seu fatorial:'))
c = n
f = factorial(n) #faz a soma com o math
print(f'Calculando {n}! ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='') #simplificado caso nao seja o numero 1 coloca x se e coloca = !
    c -= 1
#calculo do fatorial é f = f * c 
#f sendo = 1!
print(f'{f}') #fala o resultado
