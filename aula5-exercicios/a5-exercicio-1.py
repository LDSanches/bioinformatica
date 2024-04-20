# Exercicio 1 funçoes - Fatorial:
def calcular_fatorial(numero):
    fatorial = 1

    for i in range(numero, 0, -1):
        fatorial *= i

    return fatorial

numero = int(input("Digite um número: "))
fatorial = calcula_fatorial(numero)
print(f"Fatorial de {numero} é {fatorial}.")

# Outro exemplo:
def calcula_fatorial(numero):
    fatorial = 1

    while numero >= 1:
        fatorial *= numero
        numero -= 1

    return fatorial

numero = int(input("Digite um número: "))
fatorial = calcula_fatorial(numero)
print(f"Fatorial de {numero} é {fatorial}.")