'''
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro,
na ordem de colocação.
Depois mostre:
a) apenas os 5 primeiros colocados
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time da Chapecoense
'''

time = ('FLAMENGO','CRUZEIRO','RED BULL','PALMEIRAS',
        'BAHIA', 'FLUMINENSE', 'ATLETICO MG','BOTAFOGO',''
        'MIRASSOL','CORINTHIAS','GREMIO','CEARÁ','VASCO',
        'SÃO PAULO','EC VITORIA','INTERNACIONAL','FORTALEZA',
        'EC JUVENTUDE','RECIFE')
print('-=-'*10)
print('Tabelas DE Time BRASILEIRÃO')
print('-=-'*10)
print(f'Times do Brasileirão: {time}')
print('-=-'*10)
print(f'Os 5 Primeiros Times: {time[0:5]}')
print('-=-'*10)
print(f'Os ultimos 4 Times: {time[-4:]}')
print('-=-'*10)
print(f'Os Times em ordem Alfabetica: {sorted(time)}')
print('-=-'*10)
print(f'O Corinthias esta na posição: {time.index("CORINTHIAS")+1}') #index faz o mostra alguma palavra em tal posição!
print('-=-'*10)