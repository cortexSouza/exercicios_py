# Faça um programa que leia o comprimento do cateto oposto e cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

'''cos = float(input('Digite o valor do cateto oposto: '))
sen = float(input('Digite o valor do cateto adjacente: '))
h = (cos**2+sen**2)**(1/2)
print('-'*24,'\nO cateto oposto vale {}\nO cateto adjacente vale {}\nHipotenusa (Tangente) vale {:.2f}'.format(cos,sen,h))'''

from math import hypot
cos = float(input('Qual a medida do Cateto Oposto?: '))
sin = float(input('Qual a medida do Cateto Adjacente?: '))
tan = hypot(cos,sin)
print('A Tangente mede: {:.2f}'.format((tan))) 