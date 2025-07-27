#import - seria para importar uma coisa ex import math = importar matematica 
#from match import sqrt =   que seria para importar somente 1 coisa ou mais desejada
from math import sqrt
num = int(input('Digite um Numero:'))
raiz = sqrt(num) #importa a raiz quadrada sqrt!
print(f'A Raiz Quadrada de {num} é {raiz:.2f}')