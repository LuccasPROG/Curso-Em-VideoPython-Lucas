''' Crie um programa que leia o ano de nascimento de sete pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''
from datetime import date
atual = date.today().year
totm = 0
totc = 0
for pessoa in range(1, 8):
    nasc = int(input(f'Digite o Ano a {pessoa}° pessoa Naceu:'))
    idade = atual - nasc
    if idade >= 18:
        totm += 1
    else:
        totc += 1
print(f'O numero de Pessoas maior de Idade é {totm}')
print(f'O Numero de Pessoas Jovens é de {totc}')