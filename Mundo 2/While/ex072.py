''' Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar 999,
que é a condição de parada (flag).
No final, mostre quantos números foram digitados
e qual foi a acc entre eles (desconsiderando o flag)
'''

n = soma = cont = 0
while True: #fica em loop infinity
    n = int(input('Digite um Numero:[999 Para Parar!!]'))
    if n == 999:
        break #break parar o enquanto quando n for 999 = frag
    soma += n
    cont += 1
print(f'Os {cont} Numeros Digitos Somado é {soma}')