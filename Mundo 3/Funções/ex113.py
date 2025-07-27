"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""
def fatorial(num=1, show=False):
    """
    -> Calcula o Fatorial de Um Numero Digitado!
    num -> e o numero digitado
    show -> é opicional ele mostra os numeros bonitos = true ou false
    return -> o fatorial de f
    """
    f = 1
    for c in range(num, 0, -1) :
        if show:
            print(f'{c}',end='')
            if c > 1:
                print(f' x ',end='')
            else:
                print(f' = ',end='')
            
            
        f *= c
    return f
#Inicio:
num = int(input('Digite um Numero:'))
print(fatorial(num, show=True))