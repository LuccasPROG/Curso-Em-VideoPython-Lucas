"""Reescreva a função `leiaInt()` que fizemos ,
incluindo agora a possobilidade da digitação de um número de tipo inválido.
Aproveite e crie também a função `leiaFloat()` com a mesma funcionalidade."""
def leiaint(msg):
    while True:
        try:
            leia = int(input(msg))
        except KeyboardInterrupt: # exessão, caso de error fazer o que! 
            print('\033[0;31mO usúario preferiu não informar os dados!\033[m')
            return 0
        except:
            print('\033[0;31mErro: Digite um Numero inteiro valido!\033[m')
            continue
        else:
            return leia
def leiareal(msg):
    while True:
        try:
            real = float(input(msg))
        except KeyboardInterrupt:
            print('\033[0;31mO usúario preferiu não informar os dados!\033[m')
            return 0
        except:
            print('\033[0;31mErro: Digite um Numero Real Valido!\033[m')
            continue
        else:
            return real
#Inicio:
inteiro = leiaint('Digite um Numero Inteiro:')
real = leiareal('Digite um Numero Real:')
print(f'O número inteiro foi {inteiro} e o número real foi {real}')