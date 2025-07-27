'''
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso de zero até vinte

Seu programa deverá ler um número pelo teclado
(entre 0 e 20)
e mostrá-lo por extenso'''

cont = ('zero','um','dois','tres','quatro','cinco','seis','sete',
        'oito','nove','dez','onze','doze','treze','quatoze','quinze',
        'dezeseis','dezesete','dezoito','dezenove','vinte')
print('=-' * 15)
print('     NUMEROS POR EXTENSO')
print('=-' * 15)
while True:
    while True:
        num = int(input('Digite um Numero entre (0 e 20):'))
        if 0 <= num <= 20:
            break
        print('Tente novamente ',end='')
    print(f'Você digitou o numero {cont[num]}')
    opcao = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
    if opcao == 'N':
        break
print('Programa Finalizado')