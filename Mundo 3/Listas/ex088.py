'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''
lista = list()
par = list()
impares = list()
while True:
    num = int(input('Digite um Numero:'))
    lista.append(num)
    resp = (input('Deseja Continuar?[S/N]:')).strip().upper()[0]
    if resp == 'N':
        break
for num in lista:
    if num % 2 == 0:
        par.append(num)
    elif num % 2 == 1:
        impares.append(num)

print(f'A lista Completa é :{lista}')
print(f'A Lista com Pares é {par}')
print(f'A lista com impares é {impares}')
