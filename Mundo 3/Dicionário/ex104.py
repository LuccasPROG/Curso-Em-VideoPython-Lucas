"""
Aprimore o DESAFIO 102 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes de aproveitamento 
de cada jogador.
"""
info = dict()
time = list()
gols = list()
while True:
    info.clear()
    info['nome'] = str(input('Digite o Jogador:'))
    partidas = int(input(f'Quantas Partidas {info['nome']} jogou? '))
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'    Quantos Gols na {c + 1}º Partida ?:')))
    info['gols'] = gols[:]
    info['total'] = sum(gols)
    time.append(info.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar ? [S/N]:')).strip().upper()[0]
        if resp not in 'SN':
            print('Erro! Digite S ou N!')
    if resp == 'N':
        break
print('-='*25)
print('Cod.', end='')
for i in info.keys(): #mostra so as variaveis
     print(f'{i:<15}',end='')
print()
print('-' * 40)
for c, v in enumerate(time):
    print(f'{c:>3} ', end='')
    for k in v.values(): #mostra so oq tem dentro das variaveis
          print(f'{str(k):<15}', end='')
    print()
while True:
    busca = int(input('Quer ver o Codigo de qual jogador ? (999 para parar!)'))
    if busca == 999:
          break
    if busca >= len(time):
          print(f'Erro, Jogador Não Encontrado com o Codigo {busca}')
    else:
        print('-'* 35)
        print(f'Informação do Jogador {time[busca]["nome"]}:')
        print('-'* 35)
        for i, k in enumerate(time[busca]["gols"]):
             print(f'   No jogo {i+1} Fez {k} Gols.')
        print('-'*35)
print('>>>> Volte Sempre <<<<')