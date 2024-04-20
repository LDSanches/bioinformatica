# """
# #### Exercício 1
# 
# Receba um número e calcule o fatorial dele.
# 
# Obs: O fatorial de um número é calculado pela seguinte fórmula "n! = n · (n-1) · (n-2) … 3 · 2 · 1". Ou seja, por exemplo:
# 
# 4! = 4 * 3 * 2 * 1 = 24.
# 
# Exemplo:
# 
# Digite um número:
# 4
# 
# O fatorial de 4 é 24.
# --------
# Digite um número:
# 5
# 
# O fatorial de 5 é 120.
# 
# Dica: Para ajudar nesse cálculo, lembre-se das estruturas de repetição. 
# 
# Pode-se utilizar o comando "while" ou até o "for" para te ajudar nisso.
# 
# Fonte: Curso em vídeo.
# """

n_inicial = int(input('Digite um número: '))
#n_range = 1
for n_range in range(n_inicial):
    if n_range == 1:
        n_fator = n_inicial * (n_inicial - n_range)
    elif n_range > 1:
        n_fator = n_fator * (n_inicial - n_range)
    n_range += 1
    #print(n_fator)

print(f'O fatorial de {n_inicial} é {n_fator}.')

numero = int(input ("Digite o número: "))
resposta = 1


# Outro exemplo com FOR:
numero = int(input('Digite um número: '))

for i in range(numero, 0, -1):
    resposta = resposta * i

print(f"0 fatorial de {numero} é {resposta}.")


# Outro exemplo com WHILE:
numero = int(input('Digite um número: '))
fatorial = 1

while numero >= 1:
    fatorial *= numero
    numero -= 1

print(f"0 fatorial de {numero} é {resposta}.")
