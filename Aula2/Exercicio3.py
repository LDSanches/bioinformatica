# Exercise 3
price_number = float(input('Digite o preço do produtos em reais R$ 1999.99: R$ '))
desc_number = int(input('Digite o desconto a ser aplicado (em porcentagem): '))

total_desc_price = float(price_number * (desc_number / 100))
total_price = float(price_number - total_desc_price)

print('O preço final do produto é: R$', total_price)
