"""
Crie um programa onde o usuário possa digitar
sete valores numéricos
e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares.

No final, mostre os valores pares e ímpares
em ordem crescente.
"""
lista = [[], []]
num = 0
for c in range(1,8):
    num = (int(input(f'Digite o {c}° Valor:')))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print('-=-' * 20)
lista[0].sort()
lista[1].sort()
print(f'Todos os Numeros Par digitados é {lista[0]}')
print(f'Todos os Numeros Impares digitados é {lista[1]}')
