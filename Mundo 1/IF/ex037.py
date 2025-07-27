#crie um script que ve o maior valor e o menor valor digitado!
a = int(input('Primeiro Valor:'))
b = int(input('Segundo Valor:'))
c = int(input('Terceiro Valor:'))
#procurando quem é o valor menor !
menor = a
if b<a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#procurando quem é o maior valor !
maior = a
if b > a and b > c: 
    maior = b
if c > a and c > b:
    maior = c
print(f'O Menor Valor digitado é: {menor}')
print(f'O Maior valor digitado é: {maior}')
