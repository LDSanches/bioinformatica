# Exercicio 
# Vamos fazer dois exercícios que já fizemos, mas usando funções.
# 1) Façam uma função para aquele exercício que recebe uma base 
#    e retorna sua base complementar (exemplo: 'A' -> 'T').
# 2) Depois façam uma outra função que recebe uma string com 
#    tamanho qualquer de par de bases e retorna o complemento dela 
#    (exemplo: 'ATATTC' -> 'TATAAG'). Ela vai utilizar a função 1.

# Podem consultar resoluções passadas se quiserem: a única regra é que 
# a segunda função necessariamente vai usar a primeira função em vez de reescrever a lógica.

def conversor_sequencial(sequencia):

    conversor = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G",
    }

    return conversor[sequencia]

def conversor_sequencial_multi(sequencias):
    sequencia_final = ""
    for base in sequencias:
        sequencia_final += conversor_sequencial(base)

    return sequencia_final


conversor = input('Digite a sequência: ')
#print(conversor_sequencial(conversor))
print(conversor_sequencial_multi(conversor))
