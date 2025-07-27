#Iniciando aprendendo função

#+-------------------------------------------------------+
def soma(*num):
    soma = 0
    for s in num:
        soma += s
    print(f'Os Valores Somado {num} é {soma}')
soma(5,6)
soma(7,6,5)
soma(1,11,111)
#+-------------------------------------------------------+

'''def dobra(lis):
    pos = 0
    while pos < len(lis):
        lis[pos] *= 2
        pos += 1
valores = [7,2,6,4,3,9]
dobra(valores)
print(valores)'''

#+-------------------------------------------------------+

'''def cont(*num):
    total = len(num)
    print(f'Os Numeros {num} o total foi {total}', end=' ')
    print('Fim!')
cont(7, 5)
cont(10, 6, 5)
cont(1)
cont(8, 9, 4, 0)'''
#+-------------------------------------------------------+

'''def f(msg):

    print('-='* 20)
    print(msg)
    print('-=' * 20)
for c in range(0,3):
    f(str(input('Digite sua Mensagem:')))'''
#+-------------------------------------------------------+