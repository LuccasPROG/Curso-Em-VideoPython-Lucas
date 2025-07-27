''' Refaça o desafio da taboada do mundo 1, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for'''
from time import sleep
print('-=' * 20)
print('               TABUADA')
print('-=' * 20)
n = int(input('Digite um Numero Para Sua Taboada:'))
print('Analizando.')
sleep(0.5)
print('Analizando. .')
sleep(0.5)
print('Analizando. . .')
sleep(0.5)
for c in range(1, 11):
    print(n, 'x',c, '=', c * n)