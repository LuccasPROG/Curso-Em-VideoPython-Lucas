'''
Refaça o DESAFIO 56, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando
a estrutura while
'''
print('Gerador de PA') #mesmo exercicio usado no 56 feito por outra estrutura enquanto ! while
print('=-=' * 20)
primeiro = int(input('Primeiro Termo:'))
razao = int(input('Razão:'))
termo = primeiro #termo passa a setorna o primeiro termo
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    cont += 1
print('Fim')