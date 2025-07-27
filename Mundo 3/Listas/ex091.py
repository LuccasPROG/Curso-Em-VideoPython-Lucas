#crie 2 listas que ve o nome e idade e verifica se e maior de idade e mostra todos os maiores de idade!
lista = list()
dado = list()
maior = menor = 0
for temp in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    lista.append(dado[:])
    dado.clear()

for p in lista:
    if p[1] >= 18:
        print(f'{p[0]} é Maior de Idade!')
        maior += 1
    else:
        print(f'{p[0]} é Menor de Idade!')
        menor += 1

print(f'Ao todo temos {maior} Maior e {menor} Menor de idade!')





'''nome = [['barbara', 29],['Manu', 24], ['Lucas', 19], ['Valentina', 7]]
print(nome[0][0])
for p in nome:
    print(f'{p[0]} Tem {p[1]} Anos de Idade')'''

#-===========================================================================-

'''nome = list()
nome.append('Lucas')
nome.append(19)
galera = list()
galera.append(nome[:])
nome[0] = 'Suelen'
nome[1] = 34
galera.append(nome[:])
print(galera)'''