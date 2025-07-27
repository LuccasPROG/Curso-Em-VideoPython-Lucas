'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla.
No final, mostre:

a) quantas vezes apareceu o valor 9
b) em que posição foi digitado o primeiro valor 3
b) quais foram os números pares
'''
n = (int(input('Digite um Numero:')), #tuplas, 4 numeros digitados
     int(input('Digite outro Numero:')),
     int(input('Digite mais um Numero:')),
     int(input('Digite o ultimo Numero:')),)
print(f'Os Valores Digitados foi: ',end='')
for c in n:
    print(f'{c} ', end='')
print(f'\nO valor 9 apareceu {n.count(9)} vezes') #conta quantas vezes apareceu o numero 9 
if 3 in n: # verifica se tem realmente 3 na tupla
    print(f'Posição do Primeiro Numero 3 Digitado : {n.index(3)+1}') #mostra em que posição o prmeiro numero 3 foi digitado!
else: # se nao tiver numero 3 aparece nao encontrado
    print('O Numero 3 não foi encontrado!')
print(f'Numeros Pares Encontrados Foram :', end='')#mostra quantos numeros foram encontrado na tupla que sao pares !
for p in n: #faz o for para aparecer os numeros digitados que forem parres 
    if p % 2 == 0:
        print(p,end=' ')