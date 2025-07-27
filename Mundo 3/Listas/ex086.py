'''
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()).

No final, mostre a lista ordenada na tela.
'''
lista = list()
for c in range(0,5):
    numero = int(input('Digite um Numero:'))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista!')
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos , numero)
                break
            print(f'Adicionado ao posição {pos} da lista')
            pos += 1
print('-=-'*10)
print(f'Os Valores em Ordem foram {lista}')