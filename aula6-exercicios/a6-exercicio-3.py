"""
Exercício 3 - Calculando a média de uma lista

Escreva uma funcao chamada `calcular_media` (sem acento) que recebe uma lista com numeros
e retorne a média dos valores dela.

Exemplo de uso:
>>> print(calcular_media([0, 100, 200]))
>>> 100
"""

def calcular_media(lista_de_numeros):
    #tamanho_lista = len(lista_de_numeros)
    valor_total = 0
    for i in range(len(lista_de_numeros)):
        valor_total = (lista_de_numeros[i] + valor_total)
    
    media_valores = (valor_total / len(lista_de_numeros))
    return media_valores

#print(calcular_media([0, 100, 200]))
