"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.

No final, mostre o conteúdo da estrutura na tela.
"""

aluno = dict() #cria um dicionario
aluno['nome'] = str(input('Nome:'))
aluno['Media'] = float(input(f'Media de {aluno["nome"]}: '))
print('-='*15)
print('          Boletim')
print('-=' * 15)
if aluno['Media'] <= 4.9:
    aluno['Situação'] = 'Reprovado!'
elif aluno['Media'] <= 6.9:
    aluno['Situação'] = 'Recuperação!!'
else:
    aluno['situação'] = 'Aprovado!!!'
for k, v in aluno.items():  
    print(f'{k} é igual a :{v}')