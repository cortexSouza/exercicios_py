# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

l = float(input('Qual a largura da parede em metros?'))
a = float(input('Qual a altura da parede em metros?'))
ar = l*a
l = 2
r = ar/l
print('A quantidade de litros de tinta para pintar uma parede de {}m², será: {}L'.format(ar,r))

