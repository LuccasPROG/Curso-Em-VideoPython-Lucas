# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.

import random
a1 = (input('Primeiro Aluno:'))
a2 = (input('Segundo Aluno:'))
a3 = (input('Terceiro Aluno:'))
a4 = (input('Quarto Aluno:'))
a5 = (input('Quinto Aluno: '))
lista = [a1, a2, a3, a4, a5]
random.shuffle(lista)  # shuffle escolhe um na lista e embaralha ela!!
print('A Lista Escolhida Será:')
print(lista)
