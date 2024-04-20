# Exercicio 2 funcoes - Soma numeros

def soma_numeros(num1, num2, num3):
    soma_total = (num1 + num2 + num3)
    return soma_total

valor1 = int(input("Insira os numero: "))
valor2 = int(input("Insira os numero: "))
valor3 = int(input("Insira os numero: "))

print(f"Soma total {soma_numeros(valor1,valor2,valor3)}")
