''' Crie um programa que leia vários números inteiros pelo teclado
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos
O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores
'''

r = 'S'
media = quant = soma = menor = maior = 0
while r in 'Ss':
    n = int(input('Digite um Numero: '))
    soma = soma + n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        else:
            menor = n
    r = str(input('Deseja Continuar [S/N]:')).strip().upper()[0]
media = soma / quant
print(f'A Media dos Numeros Digitados é {media}')
print(f'O Menor valor digitado é {menor} e o maior é {maior}')