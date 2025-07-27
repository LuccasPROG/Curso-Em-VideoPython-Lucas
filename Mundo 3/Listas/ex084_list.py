'''
Faça um programa que leia 5 valores números e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados
e as suas respectivas posições na lista.
'''

maior = 0
menor = 0
lista = list() #lista pede abaixo
for c in range(0,5):
    lista.append(int(input(f'Digite um Numero Na Posição {c}:'))) # pede 5 numeros !
#maior = max(lista) #menor eficiente mais mais facil e econizando tempo eficiente em projetos pequenos mais em reais perde um pouco de otimização
#menor = min(lista) # mesma coisa de cima calcula o menor valor de lista digitado
    if c == 0: #opção mais realizta e mais grande mais mais eficiente em projetos grandes ! recomendavel aprender e decorar
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('-=-'* 20)
print(f'Você digitou os valores {lista}') #valores digitados
print(f'O maior Valor Digitado foi {maior} Nas Posição ',end='') #fala o maior valor digitadp
for c, v in enumerate(lista):#realiza o for para saber a posição em que o maior foi encontrado
    if v == maior:
        print(f'{c} . .',end='')
print(f'\nO Menor Valor Digitado foi {menor} Nas Posição ',end='')#fala o menor valor digitadp
for m,x in enumerate(lista):#realiza o for para saber a posição do menor foi encontrado
    if x == menor:
        print(f'{m} . .',end='')


'''a = [2,6,5,17]
b = a[:]
b[2] = 8
print(f'A Lista A:{a}')
print(f'A Lista B:{b}')'''