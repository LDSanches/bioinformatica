import math

def aplicar_formula_de_baskara(a, b, c):
    # Calcula do delta:
    delta = (b ** 2) - (4 * a * c)

    # Verificar se o delta é negativo, zero, ou positivo
    if delta > 0:
        x1 = (-b + math.sqrt(delta) / (2*a))
        x2 = (-b - math.sqrt(delta) / (2*a))
        # return x1, x2,
    elif delta == 0:
        x1 = (-b / (2*a))
        # return x1,
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        #return
    
    return x1, x2


def aplicar_formula_de_baskara_michel(a, b, c):
    # Calcula do delta:
    delta = (b ** 2) - (4 * a * c)

    # Verificar se o delta é negativo, ou positivo
    if delta < 0:
        return
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
    
    return x1, x2


print(aplicar_formula_de_baskara_michel(3, -2, -8))