"""
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta.

No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente

"""

"""
Cria um programa que lê nome e duas notas de vários alunos
e guarda-os numa lista completa.
"""
notas = list()
media = 0
while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1 + nota2) / 2
    notas.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja Continuar ?[S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 20)
print(f'{'NO.':<4} {'Nome':<10} {'Media':>8}')
print('-'*26)
for i, n in enumerate(notas):
    print(f'{i:<4} {n[0]:<10} {n[2]:>8.1f}')
while True:
    print('-='*21)
    opcao = int(input('Deseja ver a Nota de Qual Aluno? (999 Interrompe!) :'))
    if opcao == 999:
        print('Finalizando . . .')
        break
    if opcao <= len(notas) - 1:
        print(f'As Notas de {notas[opcao][0]} São {notas[opcao][1]}')
print('>>>>>> Volte Sempre <<<<<')