"""
Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.

No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado
"""
from random import randint 
from time import sleep
from operator import itemgetter
jogo = {'jogador1':randint(1,6),
        'jogador2':randint(1,6),
        'jogador3':randint(1,6),
        'jogador4':randint(1,6)}
print(('-=' * 15))
print('      Valores Sorteados')
print('-=' *15)
for k, v in jogo.items():
    print(f'{k} Jogou {v}')
    sleep(1)
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1),reverse=True)
print('-=' * 15)
print('     RANKING JOGODADORES')
print(('-=' * 15))
for k, v in enumerate(ranking):
    print(f'{k + 1}º Lugar {v[0]} com {v[1]}')
    sleep(1)
print(('-=' * 15))
print()