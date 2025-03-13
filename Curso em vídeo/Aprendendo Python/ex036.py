'''
Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.
'''

valor_casa = float(input('Qual o valor da casa?: '))
salario = float(input('Qual o seu salário?: '))
anos_pagamento = float(input('Em quantos anos você pretende pagar a casa? '))
valor_mensal = (valor_casa / anos_pagamento) / 12

print('Emprestimo APROVADO' if valor_mensal < salario * 0.3 else 'Emprestimo NEGADO')