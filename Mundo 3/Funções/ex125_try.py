#Inicio em TRY!
try: # tente fazer algo !
    a = int(input('Digite um Numero:'))
    b = int(input('Digite divisão de Numero:'))
    s = a / b
except (ValueError, TypeError):# exessão, caso de error fazer o que! 
    print('\033[0;31mTivemos um poblema com o dados que você digitou !\033[m')
except ZeroDivisionError:# exessão, caso de error fazer o que! 
    print('\033[0;31mNão foi possivel fazer divisão por zero!\033[m')
except KeyboardInterrupt:# exessão, caso de error fazer o que! 
    print('\033[0;31mO usúario preferiu não informar os dados!\033[m')
except Exception as error: # exessão, caso de error fazer o que! 
    print(f'\033[0;31mErro: o erro encontrado foi {error.__cause__}!\033[m')
else: # senão, isso é caso não de error, bom fazer para tirar o negocio grande de error no pront de cmd
    print(f'A Divisão é {s:.1f}')
finally: # finalização vai acontecer idenpendende se de error ou não !
    print('>> Obrigado, Volte sempre! <<')