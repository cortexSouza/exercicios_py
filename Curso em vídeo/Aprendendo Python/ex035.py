'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
'''

a = float(input('Valor da reta A: '))
b = float(input('Valor da reta B: '))
c = float(input('Valor da reta C: '))

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b) :
    print('É... Com essas dimensões, o triângulo vem.')
else:
    print('Não é possivel formar um retriângulo com esssas dimensões.')