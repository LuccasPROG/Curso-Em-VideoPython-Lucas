'''
Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada

No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag!)
'''
soma = num = cont = 0
num = int(input('Digite um Numero:[999 Para Parar!]'))
while num != 999:
    cont += 1
    soma = soma + num
    num = int(input('Digite um Numero:[999 Para Parar!]'))
print(f'Você digitou {cont} numeros e a soma entre eles é {soma}')
