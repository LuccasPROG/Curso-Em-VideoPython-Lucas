"""
Faça um programa que leia nome e peso de várias pessoas
guardando tudo em uma lista.
No final, mostre:

a: quantas pessoas foram cadastradas.
b: uma listagem com as pessoas mais pesadas
c: uma listagem com as pessoas mais leves

Obs.: Gerar uma lista com os mais leves e mais pesados
Vai depender de analisar qual é o mais leve e o mais pesado.
Se houver mais de um com esse peso, insere na lista.
O mais normal é que a lista de mais pesados tenha apenas 1 pessoa,
que é o motivo pelo qual a lista existe.

"""
registro = list()
temp = list() 
mais = menos = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(registro) == 0: #calcula o peso menor e maior !
        menos = mais = temp[1]
    else:
        if temp[1] > mais:
            mais = temp[1]

        if temp[1] < menos:
            menos = temp[1]

    registro.append(temp[:])#adiciona a lista temp em lista fazendo uma copia
    temp.clear()#apaga a lista temp
    resp = str(input('Deseja Continuar ?[S/N]:')).strip().upper()[0] 
    if resp in 'N':
        break
print('-=-' * 15)
print(f'Ao total tem {len(registro)} Pessoas Cadastradas!')
print(f'As pessoas mais pesadas é {mais}kg Peso de:',end=' ')
for n in registro:#escrever o nome das pessoas mais pesadas
    if n[1] == mais:
        print(f'{n[0]}')
print(f'As Pessoas mais leves é  {menos}kg Peso de: ',end=' ')
for n in registro:#escrever o nome das pessoas mais leves
    if n[1] == menos:
        print(f'{n[0]}')
