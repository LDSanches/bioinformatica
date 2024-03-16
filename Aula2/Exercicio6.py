# Exercicio 6
# Dado apenas um par de base 'A', 'T', 'C' ou 'G', imprima na tela a base complementar
# A -> T 
# T -> A 
# G -> C 
# C -> G 

v_base = str(input('Digite seu par de base: '))

if v_base == 'A':
    print('T')
elif v_base == 'T':
    print('A')
elif v_base == 'G':
    print('C')
elif v_base == 'C':
    print('G')
