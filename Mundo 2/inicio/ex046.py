'''
Refaça o DESAFIO 46, dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:

- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes
'''

print('-=-' * 20)
print('     Analizador de Triangulos !')
print('-=-' * 20)
a = float(input('Primeiro Seguimento:'))
b = float(input('Segundo Sequimento:'))
c = float(input('Terceiro Sequimento:'))
if a < b + c and b < a + c and c < a + b:
    print('Os Sequimento Acima Podera Se Tornar um Triangulo ', end='')
    if a == b == c:
        print(f'Equilatero!')
    elif a != b != c != a:
        print(f'Escaleno!')
    else:
        print('Isosceles')
else:
    print('Os Sequimentos Acima Não Podera se Tornar um Triangulo!')
