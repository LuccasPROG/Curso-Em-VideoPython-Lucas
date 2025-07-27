"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros:
o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""
def ficha(nome,gols):   
    if nome in '':
        nome = '<Desconhecido>'
    if gols in '':
        gols = 0
    print(f'O jogador {nome} Marcou {gols} gols em Campeonato!')
    
print('-'*29)
nome = str(input('Digite o Nome do Jogador:')).strip() 
gols = str(input('Quantos Gols:')).strip()
ficha(nome,gols)