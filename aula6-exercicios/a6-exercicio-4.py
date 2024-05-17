"""
Exercício 4 - Modificando um dicionário

Complete a funcao que recebe um dicionário que contém os dados de uma pessoa.

O dicionário vai conter os campos nome, salario_fixo e pode ou não conter o campo salario_variavel.

Eu quero que adicione o campo salario_total no dicionário e retorne ele.

Se o dicionario não conter o campo salario_variavel o salario_total vai ser igual o salario_fixo, se conter
vai ser igual ao salario_fixo + salario_variavel.

Exemplo de uso:
>>> pessoa = {"nome": "Michel", "salario_fixo": 1000}
>>> print(calcular_salario(pessoa))
>>> {"nome": "Michel", "salario_fixo": 1000, "salario_total": 1000}
>>> pessoa = {"nome": "João", "salario_fixo": 10000, "salario_variavel": 2000}
>>> print(calcular_salario(pessoa))
>>> {"nome": "João", "salario_fixo": 10000, "salario_variavel": 2000, "salario_total": 12000}
"""

def calcular_salario(pessoa):
    if "salario_variavel" in pessoa:
        pessoa['salario_total'] = pessoa['salario_fixo'] + pessoa['salario_variavel']
    else:
        pessoa['salario_total'] = pessoa['salario_fixo']

    return pessoa

#pessoa = {"nome": "Michel", "salario_fixo": 1000}
#print(calcular_salario(pessoa))

#pessoa = {"nome": "João", "salario_fixo": 10000, "salario_variavel": 20000}
#print(calcular_salario(pessoa))

