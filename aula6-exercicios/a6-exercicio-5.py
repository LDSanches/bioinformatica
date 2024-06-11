"""
Exercicio 5 - Usando funcoes

Você vai escrever uma funcao que recebe uma lista com números e deve retornar uma outra lista
só com os números primos. (Parecido com o exercício 2 da aula 3).

Mas você não precisa escrever a lógica para saber se o número é primo: você pode só usar a funcão
`verificar_se_eh_primo` disponibilizada, que vai retornar True se o número for primo e False se não for.
"""

import statistics

def verificar_se_eh_primo(numero):
    if numero > 1:
        for i in range(2, int(numero / 2) + 1):
            if (numero % i) == 0:
                return False
        return True
    return False


def filtrar_lista_por_numeros_primos(lista):
    lista_filtrada = []
    for i in range(len(lista)):
        if verificar_se_eh_primo(lista[i]) == True:
            lista_filtrada.append(lista[i])

    return lista_filtrada

#print(filtrar_lista_por_numeros_primos([10, 11, 50, 13, 99, 7]))
