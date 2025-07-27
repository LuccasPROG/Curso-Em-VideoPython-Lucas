'''
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses.
Seu aplicativo deverá analisar se a expressão passada 
está com os parênteses abertos e fechados na ordem correta.
'''
exp = str(input('Digite sua Expressão:'))
lista = list()
for simbo in exp:
    if simbo == '(':
        lista.append('(')
    elif simbo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua Expressão está Valida!')
else:
    print('Sua Expressão está errada!!')
print()
