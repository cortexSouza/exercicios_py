# faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o seu salário?: '))
aumento = salario+(salario*0.15)
print('Seu salário pós aumento será de {:.2f}'.format(aumento))