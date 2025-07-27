'''
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos).
Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais
'''
palavras = ('PYTHON','PROGRAMAR','ANDAR','CORRER','MAE',
            'LEITE','VENTILADOR','COMPUTADOR','SOFT',
            'TECLADO','CAMA','MOUSE','EDSON','VALENTINA',
            'LUCAS','SUELEN','EDNA','DOG')
for p in palavras:
    print(f'\nNa Palavra {p} Temos: ',end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')