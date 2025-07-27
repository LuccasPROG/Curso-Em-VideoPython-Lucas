# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math
num = float(input('Digite um Numero:'))
print(f'o Aredontamento do numero {num} digitado é {math.trunc(num)}') # forma usando a biblioteca mathn/trunc tira os numeros decimais! 



'''num = float(input('Digite um Numero:'))
print(f'O Arendondamento do numero {num} digitado é {int(num)}')''' # mesma forma da de cima so que sem Biblioteca, mais bruta