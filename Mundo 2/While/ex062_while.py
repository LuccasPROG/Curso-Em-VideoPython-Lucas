'''
faça um script que vai digitar um valor e so vai parar caso os numeros seja diferente de 0 qt par qt im
'''
n = 1
np = ni = 0
while n != 0: #So vai parar o laço caso a numero digitado seja 0
    n = int(input('Digite um Valor:'))
    if n != 0: #caso o numero digitado seja diferente de 0 prossiga com os if 
        if n % 2 == 0:
            np += 1
        elif n % 2 == 1:
            ni += 1
print(f'A Quantidade de numeros pares é {np}')
print(f'A Quantidade de Numeros Impares é {ni}')

'''r = 'S' #resposta recebe R
while r == 'S': #So vai Parar o Laço caso a Resposta seja S
    n = int(input('Digite um Numero:'))
    r = str(input('Deseja Continuar[S/N]')).upper() #Usado para Fazer Parar a Repetição com S
print('Acabou . . !!')'''