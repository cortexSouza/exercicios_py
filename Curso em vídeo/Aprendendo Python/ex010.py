# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = int(input('Quantos dinheiros tem em sua carteira?'))
dolar = 5.88
conversão = real/dolar
print('Com R${}, você consegue trocar para ${} Dólares '.format(real,conversão))