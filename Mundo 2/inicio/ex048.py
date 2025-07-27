'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros
'''
import time
print(f'{' Lucas Store ' :=^40}')
preco = float(input('Preço Das Compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] á Vista dinheiro/cheque
[2] á Vista Cartão
[3] 2x no Cartão
[4] 3x ou mais no Cartão ''')
opcao = int(input('Digite uma Opção:'))
print('Analizando . . .')
time.sleep(2)
if opcao == 1:
    pagamento = preco - ((preco * 15)/ 100)
    print(f'Você pagou a Vista com Dinheiro/Chegue Tera 15% de Desconto!')
    print(f'Valor da Compra: R${pagamento:.2f}')
elif opcao == 2:
    pagamento = preco - ((preco * 5) / 100)
    print(f'Você pagou a Vista no Cartão e Tera 5% De Desconto!')
    print(f'Valor da Compra: R${pagamento:.2f}')
elif opcao == 3:
    parcela = preco / 2
    print(f'Você pagou 2x no Cartão !')
    print(f'Você ira parcelar de 2x de R${parcela:.2f} Sem Juros!')
    print(f'Valor da Compra: R${preco}')
elif opcao == 4:
    pagamento = preco + ((preco * 20)/ 100)
    veses = int(input('Quantas Vezez deseja Parcelar? :'))
    parcela = pagamento / veses
    print(f'Você pagou {veses}x no Cartão e tera 20% De Juros!!!')
    print(f'Você ira parcelar de {veses}x por {parcela:.2f}')
    print(f'Valor da Compra: R${pagamento:.2f}')
else:
    print('Opção Invalida, Tente Novamente!')