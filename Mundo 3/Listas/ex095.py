"""
Aprimore o desafio anterior, mostrando no final:

a: a soma de todos os valores pares digitados
b: a soma dos valores da terceira coluna
c: o maior valor da segunda linha
"""
matriz = [[0,0,0], [0,0,0,], [0,0,0]]
spar = tcolu = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um Numero na posição[{l}|{c}]: '))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
print('-='* 15)
print('         Matrizes')
print('-=' * 15)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('-=' * 15)
print(f'A Soma da Matriz Pares é: {spar}')
for l in range(0,3):
    tcolu += matriz[l][2]
print(f'A Soma do Matriz da Terceira Coluna é :{tcolu}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior numero digitado na segunda coluna é :{maior}')
