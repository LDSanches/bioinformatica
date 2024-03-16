# Exexcicio 5
# Escreva um programa que simula um radar eletrônico cuja velocidade máxima é 80 km/h. 
# Receba de input a velocidade de um carro.
# Caso ele esteja acima da velocidade permitida, imprima que ele foi multado mais o valor da multa. 
# O valor da multa deve ser de 7 reais por kilometro por hora excedido.
# No fim, deseje um bom dia para o motorista, independente da velocidade.

velocidade = float(input('Qual a velocidade do veiculo em Km/h: '))
multa_aplicada = 7
velocidade_max = 80

if velocidade > 80:
    print('Voce foi multado!')
    v_multa = ((velocidade - velocidade_max) * multa_aplicada)
    print('Valor da multa é de R$', v_multa)

print('Bom dia e dirija com cuidado!')