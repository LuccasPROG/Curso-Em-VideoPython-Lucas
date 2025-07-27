# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo

# Inclusive posso dizer qual tipo de triângulo pode ser formado.
# Não deve ser difícil isso em Python.

print('-=-' * 20)
print('     Analizador de Triangulos !')
print('-=-' * 20)
a = float(input('Primeiro Seguimento:'))
b = float(input('Segundo Sequimento:'))
c = float(input('Terceiro Sequimento:'))
if a < b + c and b < a + c and c < a + b:
    print('Os Sequimento Acima Podera Se Tornar um Triangulo')
else:
    print('Os Sequimentos Acima Não Podera se Tornar um Triangulo!')
