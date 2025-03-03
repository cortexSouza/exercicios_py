# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Qual o preço do pruduto?: '))
desconto = produto-(produto*0.05)
print('O preço com desconto fica {:.2f}'.format(desconto))