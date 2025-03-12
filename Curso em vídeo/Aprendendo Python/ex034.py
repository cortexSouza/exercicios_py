'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1250,00 calcule um aumento de 10%
Para salarios inferiores, calcule um aumento de 15%
'''

salario = float(input('Qual o seu salário?: '))
aumento_salario1 = salario + (0.10*salario)
aumento_salario2 = salario + (0.15*salario)
print('Com um aumento de 10%, você passará a receber um salário de R${}'.format(aumento_salario1) if salario >= 1250 else 'Com um aumento de 15%, você passará a receber um salário de R${}'.format(aumento_salario2))