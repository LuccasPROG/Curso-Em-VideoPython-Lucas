"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.

O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-='*20)
print('-='*4, '  JOGUE NA MEGA CENA! ','-='*4)
print('-='*20)
per = int(input('Quantos Numeros deseja Sortear? :'))
rep = 1
while rep <= per:
    cont = 0
    while True:
        alea = randint(1,60)
        if alea not in lista:
            lista.append(alea)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    jogos.append(lista[:])
    lista.clear()
    rep += 1
print('-='*20)
print('-=' * 5, f' Sorteando {per} Jogos', '-=' * 5)
print('-='* 20)
for i, l in enumerate(jogos):   
    print(f'{i+1}º JOGO: {l}')
    sleep(1)
print()