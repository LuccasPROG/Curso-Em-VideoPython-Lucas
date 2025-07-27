def aumento(preço=0,taxa=0,formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def desconto(preço=0, taxa=0,formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0,formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0,formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('-='*20)
    print('   Resumo do valor'.center(35))
    print('-='*20)
    print(f'Preço analizado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade analizado: \t{metade(preço, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumento(preço,taxaa, True)}')
    print(f'Com {taxar}% de desconto: \t{desconto(preço,taxar, True)}')
    print('-='*20)
