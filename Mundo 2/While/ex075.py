''' Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostra:
a) quantas pessoas têm mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres têm menos de 20 anos'''
pess = 0
home = 0
f = 0
while True:
    print('-=-' * 10)
    print('     CADASTRE UMA PESSOA')
    print('-=-' * 10)

    idade = int(input('Idade:'))
    if idade >= 18:
        pess = pess + 1
    sexo = ' '
    while sexo not in 'MF': #fala que enquanto a variavel sexo nao for digitado M OU F ira continuar lendo sexo
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if sexo in 'M':
        home += 1
    if sexo in 'F' and idade < 20:
        f += 1
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer Continuar? [S/N] :')).strip().upper()[0]
    if opção == 'N':
        break

print(f'Total de Pessoas Com mais de 18 Anos: {pess}!')
print(f'Ao Todo Temos {home} Homens Cadastrados!')
print(f'E Temos {f} Mulheres com Menos de 20 Anos!')