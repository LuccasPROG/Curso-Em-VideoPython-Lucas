'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.

Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
num = list()
while True:
    n = int(input('Digite um Numero para Sua Lista:'))
    if n not in num:
        num.append(n)
        print('Numero Registrado com Sucesso . . ')
    else:  
        print('Numero Duplicado, Não Irei Registrar!')
    print('-=-'*10)
    resp = (input('Deseja Continuar [S/N]:')).upper().strip()[0]
    if resp in 'N':
        break
print('-=-'*10)
num.sort()
print(f'Você digitou os Numeros : {num}')
print('-=-'*10)