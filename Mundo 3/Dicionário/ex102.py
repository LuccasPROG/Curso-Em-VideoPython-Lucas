"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""
info = dict()
gols = list()
info['nome'] = str(input('Nome do Jogador:'))
partidas = int(input(f'Quantas Partidas {info["nome"]} Jogou ? '))
for c in range(0, partidas):
    gols.append(int(input(f'    Quantos gols na {c + 1}º partida  ?')))
info['gols'] = gols[:]
info['total'] = sum(gols)
print('-=' * 30)
print(info)
print('-=' * 30)
for v, k in info.items():
    print(f'O campo {v} tem o :{k}')
print('-=' * 30)
print(f'o Jogador {info['nome']} jogou {partidas} Partidas')
for k, v in enumerate(gols):
    print(f'    => Na {k + 1}º Partida, fez {v} Gols.')
print(f'Foi um total de {info['total']} Gols.')
print('-=' * 30)
print()