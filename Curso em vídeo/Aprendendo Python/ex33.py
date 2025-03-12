'''
faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um outro número: '))
num3 = int(input('Digite outro número: '))
if num1 > num2 and num1 > num3:
    print ('O maior número é {}'.format(num1))
elif num2 > num3:
    print('O {} é o maior'.format(num2))
else:
    print('O {} é o maior número'.format(num3))
    
    
