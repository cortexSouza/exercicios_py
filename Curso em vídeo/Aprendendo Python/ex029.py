'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.
'''

vel_carro = float(input('Qual a velocidade do carro em KM/h: '))
multa = (vel_carro - 80)*7
print('Parabéns por respeitar as leis de trânsito!' if vel_carro < 80 else 'Você foi multado em R${:.2f} por estar a uma de velocidade de {}KM/h numa via que permite 80KM/h'.format(multa, vel_carro))
