"""
Crie um programa que tenha a função leia_int(), 
que vai funcionar de forma semelhante à função input do Python,
só que fazendo a validação para aceitar apenas um valor numérico.

ex.:
n = leia_int("Digite um n")
"""
def leiaint(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro valido!\033[m')
        if ok:
            break
    return valor

#INICIO:
n = leiaint('Digite um Numero:')
print(f'você acabou de Digitar o Numero {n}')
