'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- média abaixo de 5.0: reprovado
- média entre 5.0 e 6,9: recuperação
- média 7.0 ou superior: aprovado
'''
import time
n1 = float(input('Informe a Primeira Nota:'))
n2 = float(input('Informe a Segunda Nota:'))
m = (n1 + n2) / 2
print('Analizando ...')
time.sleep(1)
print(f'Tirando a Nota {n1} e {n2} Sua media será de {m:.1f}')
if m > 7:
    print(f'A Media foi de {m} e Aluno Aprovado!')
elif m >=5 and m <= 6.9:
    print(f'A Media foi de {m} e Aluno em Recuperação!')
elif m <= 4.9:
    print(f'Coma a Media de {m} Aluno esta REPROVADO!!')