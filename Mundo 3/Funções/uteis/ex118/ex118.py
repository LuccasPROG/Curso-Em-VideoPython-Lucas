#crie uma função que faz o fatorial dobro e triplo
from ex118 import matematica
num = int(input('Digite um Numero: '))
fat = matematica.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O Fatorial Dobro e Triplo de {num} é {matematica.dobro(num)}')