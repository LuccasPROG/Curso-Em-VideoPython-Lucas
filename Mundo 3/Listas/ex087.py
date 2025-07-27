'''
Crie um programa que vai ler vários números e colocá-los em uma lista
Depois disso, mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista.
'''
lista = list()
while True:
    num = int(input('Digite um Valor:'))
    lista.append(num)
    resp = (input('Deseja Continuar[S/N]:')).strip().upper()[0]
    if resp in 'N':
        break
print(f'Você Digitou {len(lista)} Elementos!')
lista.sort(reverse=True)
print(f'Os valores em Ordem Decrecente é {lista}')
if 5 in lista:
    print('O Valor 5 Faz Parte Da Lista!')
else:
    print('O Valor 5 Não Tem na lista!')