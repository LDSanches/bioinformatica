##################
##### Aula 1 #####

# print hello world
print('Hello World')


# Environments
minha_variavel = 10
print(minha_variavel)


# Environments 2
numero_digitado = input('Digite um número: ')
print('O numero digitado foi: ', numero_digitado)


# Type Data Environments
# int -> numeros inteiros 1,2,3,4 etc
print(type(2))

# float -> numeros fracionados inteiros 1.5, 1.4545 etc
print(type(3.5667))

# bool -> binario True or False
print(type(True))

# str -> para textos com aspas simples ou duplas
print(type('2'))

# Print sum
print(1 + 1) 

# Print number
print('1' + '1')


# Environment Conversion

convert_number = 1

print(float(1))
print(int(2.8))
print(int('1'))
print(str(2.8))

# Exersise:
first_number = int(input('Enter with first number: '))
secont_number = int(input('Enter with second number: '))
sum_numbers = int(first_number + secont_number)

print('The sum of the numbers is: ', first_number + secont_number)
print('The sum of', first_number, 'and', secont_number, 'is:', sum_numbers) 
print('The sum of', first_number, 'and', secont_number, 'is:', first_number + secont_number)
print(f'The sum of {first_number} and {secont_number} is: {first_number + secont_number}') 


# Aritimetic Operators
# Aritimetic Expression

# Exercise 2
user_number = int(input('Please enter with a number: '))
sub_number = int(user_number - 1)
adc_number = int(user_number + 1)
plus_number = int(user_number * 2)
raiz_number = int(user_number ** (1/2))

print('O antecessor do numero', user_number, 'é:', sub_number)
print('O sucesssor do numero', user_number, 'é', adc_number)
print('O dobro do numero', user_number, 'é', plus_number)
print('A raiz quadrada do numero', user_number, 'é:', raiz_number)


# Exercise 3
price_number = float(input('Digite o preço do produtos em reais R$ 1999.99: R$ '))
desc_number = int(input('Digite o desconto a ser aplicado (em porcentagem): '))

total_desc_price = float(price_number * (desc_number / 100))
total_price = float(price_number - total_desc_price)

print('O preço final do produto é: R$', total_price)


##################
##### Aula 2 #####

