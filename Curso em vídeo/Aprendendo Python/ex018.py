# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, consseno e tangente desse ângulo.
from math import radians, cos, sin, tan
angulo = float(input('ângulo: '))
cos = cos(radians(angulo))
sin = sin(radians(angulo))
tan = tan(radians(angulo))
print('Cosseno: {:.2f}\nSeno {:.2f}\nTangente: {:.2f}\n'.format(cos,sin,tan))  