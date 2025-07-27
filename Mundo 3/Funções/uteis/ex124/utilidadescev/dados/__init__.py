def leiaDinheiro(msg):
    valido = False
    while not valido:
        leia = str(input(msg)).replace(',','.').strip()
        if leia.isalpha() or leia == '':
            print(f'\033[0;31mErro: \'{leia}\' é Comando Invalido!\033[m')
        else:
            valido = True
            return float(leia)


            