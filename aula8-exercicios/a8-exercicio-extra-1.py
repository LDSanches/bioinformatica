"""
Exercício 1 - Calculando a área e o perímetro de um círculo

Escreva uma função calcular_area_e_perimetro_circulo que recebe o raio de um círculo e retorna a área e o perímetro dele, nessa ordem.

A área é calculado como PI vezes o raio ao quadrado.

O perímetro é calculado como 2 vezes PI vezes o raio.

Obs: Você consegue o valor de PI na biblioteca math, usando math.pi. Não esqueça de importar ela!
"""

import math

def calcular_area_e_perimetro_circulo(raio):
    area = math.pi * (raio ** 2)
    perimetro = 2 * math.pi * raio
    return area, perimetro

# Teste igual ao test_exercicios.py:

#area = round(calcular_area_e_perimetro_circulo(10)[0])
#perimetro = round(calcular_area_e_perimetro_circulo(10)[1])

#area = round(calcular_area_e_perimetro_circulo(3)[0])
#perimetro = round(calcular_area_e_perimetro_circulo(3)[1])

#print(f"Área: {area}")
#print(f"Perímetro: {perimetro}")