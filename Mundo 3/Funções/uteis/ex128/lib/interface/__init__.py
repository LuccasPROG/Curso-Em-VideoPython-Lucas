def leiaint(msg): # le um numero!
 while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt: # exessão, caso de error fazer o que! 
            print('\033[0;31mO usúario preferiu não informar os dados!\033[m')
            return 0
        except:
            print('\033[0;31mErro: Digite um Numero inteiro valido!\033[m')
            continue
        else:
            return n

def linha(tam=42): # cria uma linha
    return '=' * tam

def cabeçalho(txt): # cria um cabeçalho
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista): # cria um menu !
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;33m{c}\033[m - \033[1;34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[1;33mSua Opção:\033[m')
    return opc
