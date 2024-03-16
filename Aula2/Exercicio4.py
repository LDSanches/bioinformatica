# Exercicio 4
idade = int(input('Qual a sua idade? '))
idate_maior_18 = idade >= 18

if idate_maior_18:
    print('Aceita algum drink?')
else:
    print('Aceita refrigerante ou água?')

print('Obrigado e volte sempre!')


if not idate_maior_18:
    print('Aceita refrigerante ou água?')

print('Obrigado e volte sempre!')
