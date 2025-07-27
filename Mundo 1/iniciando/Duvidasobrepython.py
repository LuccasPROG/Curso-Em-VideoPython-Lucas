#duvidas geral para lembrar

# ========================================
#           TIPOS PRIMITIVOS
# ========================================

# int   - Números inteiros
# float - Números reais (com casas decimais)
# bool  - Booleano (True ou False)
# str   - Texto (string / cadeia de caracteres)

# ========================================
#     ORDEM DE PREFERÊNCIA DOS OPERADORES
# ========================================

# 1 - ()          → Parênteses
# 2 - **          → Potência
# 3 - *, /, //, % → Multiplicação, Divisão, Divisão Inteira, Resto da divisão
# 4 - +, -        → Adição e Subtração

# ========================================
#              CORES NO TERMINAL
# ========================================

# Formato: \033[<número>m
# Exemplo:
print("\033[32mEsse texto é verde!\033[m")  # Cor verde

# Cores de TEXTO (30 a 37):
# 30 → Preto
# 31 → Vermelho
# 32 → Verde
# 33 → Amarelo
# 34 → Azul
# 35 → Roxo (Magenta)
# 36 → Ciano
# 37 → Branco

# Cores de FUNDO (40 a 47):
# 40 → Fundo Preto
# 41 → Fundo Vermelho
# 42 → Fundo Verde
# 43 → Fundo Amarelo
# 44 → Fundo Azul
# 45 → Fundo Roxo
# 46 → Fundo Ciano
# 47 → Fundo Branco

# Estilos (1 a 7):
# 1 → Negrito
# 2 → Fraco/opaco
# 3 → Itálico
# 4 → Sublinhado
# 5 → Piscando
# 6 → Inversão de cor
# 7 → Texto negativo/invertido

# Exemplo completo:
print("\033[1;33;44mTexto amarelo em fundo azul e negrito\033[m")

# ========================================
#                 TUPLAS
# ========================================

# Tuplas são como listas, mas IMUTÁVEIS (não dá para alterar valores depois de criadas)
# Usadas para armazenar múltiplos valores em uma única variável

lanche = ('Hamburguer', 'Suco', 'Lasanha', 'Frango', 'Batata')

# FORMA 1 – Básica
for comida in lanche:
    print('Irei comer', comida)

# FORMA 2 – Usando índice com range() e len()
for cont in range(0, len(lanche)):
    print(f'Irei comer {lanche[cont]} na posição {cont}')

# FORMA 3 – Usando enumerate()
# enumerate() retorna o índice (posição) e o valor
# pos = posição | comida = valor naquela posição
for pos, comida in enumerate(lanche):
    print(f'Irei comer {comida} na posição {pos}')

# Ordenar a tupla (gera uma LISTA nova ordenada)
print(sorted(lanche))  # ['Batata', 'Frango', 'Hamburguer', 'Lasanha', 'Suco']
print(lanche)          # Tupla original continua igual

# ========================================
#         FATIAMENTO DE STRING
# ========================================

nome = 'Python'

print(nome[0:3])    # 'Pyt' – Vai do índice 0 até o 2
print(nome[::2])    # 'Pto' – Vai de 2 em 2 (pulando)

# ========================================
#         ANÁLISE DE STRING
# ========================================

print(len('curso'))                # Conta total de caracteres → 5
print('banana'.count('a'))         # Conta quantas vezes 'a' aparece → 3
print('banana'.find('na'))         # Mostra a posição onde começa → 2
print('na' in 'banana')            # Verifica se existe dentro do texto → True

# ========================================
#     TRANSFORMAÇÕES DE STRING
# ========================================

print('python'.replace('py', 'cy'))             # Troca 'py' por 'cy' → 'cython'
print('curso'.upper())                          # Tudo em MAIÚSCULO → 'CURSO'
print('CURSO'.lower())                          # Tudo em minúsculo → 'curso'
print('python é legal'.capitalize())            # Só a primeira letra maiúscula
print('python é legal'.title())                 # Primeira letra de cada palavra
print('  curso  '.strip())                      # Remove espaços do começo e fim

# ========================================
#         JUNÇÃO DE STRINGS (join)
# ========================================

print('-'.join('ABCD'))                         # Resultado: 'A-B-C-D'
print(' '.join(['Python', 'é', 'top']))         # Resultado: 'Python é top'

tupla = [1,7,3,31]
tupla[2] = 10
tupla.append(2)
tupla.sort(reverse=True)
tupla.insert(2, 2)
if 2 in tupla:
    tupla.remove(2)
else:
    print('Nao Encontri o Numero 2 !')
print(tupla)
print(f'Essa Lista tem {len(tupla)} Elementos!')