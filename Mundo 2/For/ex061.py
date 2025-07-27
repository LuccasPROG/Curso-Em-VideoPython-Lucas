''' Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos
 '''
idadeg = 0
mediaidade = 0
maioridadehomen = 0
homenvelho = ''
totm20 = 0
for p in range(1,5):
    print(f'---------- {p}° ----------')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).upper().strip()
    idadeg += idade
    if p == 1:
        maioridadehomen = idade
        homenvelho = nome
    if sexo == 'M' and idade > maioridadehomen:
        maioridadehomen = idade
        homenvelho = nome
    if sexo == 'F' and idade <= 20:
        totm20 += 1
idadem = idadeg / 4
print(f'A media da Idade Do Grupo é de {idadem}')
print(f'O Homen mais velho é {homenvelho} e tem {maioridadehomen} Anos')
print(f'O Numero de Mulheres Abaixo de 20 Anos é de {totm20}')
