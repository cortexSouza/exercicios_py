#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos KMs o carro rodou?: '))
dias = int(input('POr quantos dias foi alugado?: '))
preco = km*0.15+dias*60
print('O valor a pagar é de:',preco)