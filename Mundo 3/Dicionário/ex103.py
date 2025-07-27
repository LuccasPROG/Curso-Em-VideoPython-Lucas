"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista.

No final, mostre:
a. Quantas pessoas foram cadastradas
b. A média de idade do grupo
c. uma lista com todas as mulheres
d. uma lista com todos os homens 
f. uma lista com todas as pessoas com idade acima da média.
"""
info = dict()
dados = list()
media = soma = 0
while True:
    info.clear()
    info['nome'] = str(input('Digite Seu Nome:'))
    sexo = ''
    while sexo not in 'FM': # faz repitir a pergunta ate que S OU M Seja Digitado
        sexo = str(input('Digite Seu Sexo:')).strip().upper()[0]
        if sexo not in 'FM':
            print('Erro! Responda Somente com M ou F !')
    info['sexo'] = sexo
    info['idade'] = int(input('Digite sua Idade:'))
    soma += info['idade']
    dados.append(info.copy())
    resp = ' '
    while resp not in 'SN': # faz rodar ate o escrito s ou n somente !! lembra disso lucas
        resp = str(input('Deseja Continuar?[S/N] :')).strip().upper()[0]
        if resp not in 'SN':
            print('Erro! Responda Somente com S ou N !')
    if resp == 'N':
        break
print('-=' *15)
print('    Informações Cadastradas')
print('-='* 15 )
media = soma / len(dados)
print(f'A)Ao Todo Temos {len(dados)} Cadastrados.')
print(f'B)As Media de Idade é de {media:.2f} anos.')
print(F'C)As Mulheres Cadastradas foram: ', end='')
for s in dados:
    if s['sexo'] in 'F':
        print(f'{s["nome"]} ', end='')
print()
print(f'D) Os Homens Cadastrados foram: ', end='')
for s in dados:
    if s['sexo'] in 'M':
        print(f'{s['nome']} ', end='')
print()
print('F) As pessoas acima da media foram ; ')
for s in dados:
    if s['idade'] >= media:
        print('     ', end='')
        for k,v in s.items():
            print(f'{k} = {v};', end='')
        print()
print('-='* 15)
print('<<< Encerrando! >>>')