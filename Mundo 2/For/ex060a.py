#aprimorado o desafio 60
maior = menor = cont = m = s = 0
mnome = menornome = ''
primeiro = True
while True:
    nome = str(input('Digite o Nome:'))
    peso = float(input('Digite o Peso:'))
    if primeiro:
        maior = menor = peso
        mnome = menornome = nome
        primeiro = False
    else:
        if peso > maior:
            maior = peso
            mnome = nome
        if peso < menor:
            menor = peso
            menornome = nome
    cont += 1
    s += peso
    m = s / cont
    opçao = ' '
    while opçao not in 'SN':
        opçao = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    if opçao == 'N':
        break
print(f'Pessoas Cadastradas : {cont}')
print(f'A pessoa com maior peso é {mnome} com {maior}kg')
print(f'A pessoa com menor peso é {menornome} com {menor}kg')
print(f'As MEDIA de pessos digitados é {m}')