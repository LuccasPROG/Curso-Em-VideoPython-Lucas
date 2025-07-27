#Mais sobre funcões e as aspas help(cont)
def fatorial(f=1):
    fac = 1
    for c in range(f, 0, -1):
        fac *= c
    return fac

num = int(input('Digite um Numero:'))
print(f'O Fatorial de {num} é {fatorial(num)}')


'''def soma(a=0, b=0, c=0):
    s = a+b+c
    return s

#Inicio:
r1 = soma(7, 6)
r2 = soma(1, 12, 4)
r3 = soma(21, 45)

print(f'Os Valores Digitados Foram {r1}, {r2}, e {r3}')'''






'''from time import sleep
def cont(i,f,p):
    """
    Programa que faz contar do inicio ate o final pulando de tanto en tanto 
    usuario que decide ex: cont(1,10,1)
    i = inicio
    f = final
    p = passo
    Feito por By: Darkness!
    """
    cont = i
    while cont <= f:
        sleep(0.5)
        print(f'{cont}',end='. ',flush=True)
        cont+= p
    sleep(0.5)
    print('Fim')
help(cont)'''