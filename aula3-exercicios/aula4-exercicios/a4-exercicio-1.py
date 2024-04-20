# Exercício 1 - Achando a base complementar:

conversor = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G",
}

sequencia_inicial = input('Digite a sequência: ')
sequencia_final = ""

for base in sequencia_inicial:
    sequencia_final += conversor[base]

print(sequencia_final)
